#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Importa arquivos do CIHA
"""
import os
import time
import datetime
from infosus import db
from infosus.ftp import FtpClient, FtpError
from infosus.importa_dbf import importaDbf
from infosus.arquivodbc import dbc2dbf
from infosus.hash import md5_arquivo

def importa_ciha(estado, ano, mes):
    print("Importando CIHA de {} do mes {} ano {}".format(estado, mes, ano))
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    print(BASE_DIR)

    conn = db.get_conn()
    cur = conn.cursor()

    sql = "select * from arquivo_dados where tipo = 'CIHA' and sub_tipo = 'CIHA' and ano = %s and (data_hora_alt > dt_importacao or dt_importacao is NULL) order by estado, ano, mes"
    cur.execute(sql, (ano,))

    rows = cur.fetchall()

    for arq_dados in rows:
        ini = time.time()
        tmp_dir = BASE_DIR + os.sep + 'tmp' + os.sep
        arq_ftp = arq_dados['caminho'] + arq_dados['nome']
        dbc_local = tmp_dir + arq_dados['nome']
        dbf_local = tmp_dir + arq_dados['nome'][:-3]+'dbf'

        try:
            ftp = FtpClient('ftp.datasus.gov.br', 'anonymous', 'tabwin@tabwin.com.br')
            ftp.download(arq_ftp, dbc_local)
        except FtpError:
            print("Erro no download do arquivo")

        expandedbc = dbc2dbf(dbc_local, tmp_dir)
        if (expandedbc == 0):
            print('Importando arquivo {} '.format(dbf_local,))
            cur.execute("delete from dados.ciha where ano = %s and id_arqdados = %s", (ano, arq_dados['id'],))
            qtd = importaDbf(conn, dbf_local, 'ciha', arq_dados['id'])
            data_hora = datetime.datetime.now()
            hash_md5 = md5_arquivo(dbc_local)
            upd = "update arquivo_dados set hash_md5 = %s, dt_importacao = %s, qt_registros = %s where id = %s"
            cur.execute(upd, (hash_md5, data_hora, qtd, arq_dados['id']))

        os.remove(dbc_local)
        os.remove(dbf_local)
        conn.commit()
        fim = time.time()
        print("Qtd Registros: {} / Tempo : {} seg".format(qtd, fim - ini))

    cur.close()
    conn.close()
