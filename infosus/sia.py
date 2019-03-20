#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Importa arquivos do SIA
"""
import os
import time
import datetime
from infosus import db
from infosus.ftp import FtpClient
from infosus.importa_dbf import importaDbf
from infosus.arquivodbc import dbc2dbf
from infosus.hash import md5_arquivo
from infosus.dbf2sqlite import dbfsia2sqlite
import sqlite3

def importa_sia_sqlite(estado, ano, mes):
    print("Importando SIA de {} do mes {} ano {}".format(estado, mes, ano))
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    print(BASE_DIR)

    conn = db.get_conn()
    cur = conn.cursor()

    sql = "select * from arquivo_dados where tipo = 'SIA' and sub_tipo = 'PA' and ano = %s and data_hora_alt > dt_importacao order by estado, ano, mes"
    cur.execute(sql, (ano,))

    rows = cur.fetchall()

    for arq_dados in rows:
        ini = time.time()
        tmp_dir = BASE_DIR + os.sep + 'tmp' + os.sep
        arq_ftp = arq_dados['caminho'] + arq_dados['nome']
        dbc_local = tmp_dir + arq_dados['nome']
        dbf_local = tmp_dir + arq_dados['nome'][:-3]+'dbf'

        ftp = FtpClient('ftp.datasus.gov.br', 'anonymous', 'tabwin@tabwin.com.br')
        ftp.download(arq_ftp, dbc_local)

        expandedbc = dbc2dbf(dbc_local, tmp_dir)
        if (expandedbc == 0):
            print('Importando arquivo {} '.format(dbf_local,))
            qtd = dbfsia2sqlite(dbf_local, arq_dados['nome'])

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

def importa_sia(estado, ano, mes):
    print("Importando SIA de {} do mes {} ano {}".format(estado, mes, ano))
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    print(BASE_DIR)

    conn = db.get_conn()
    cur = conn.cursor()

    sql = "select * from arquivo_dados where tipo = 'SIA' and sub_tipo = 'PA' and ano = %s and hash_md5 is NULL order by estado, ano, mes"
    cur.execute(sql, (ano,))

    rows = cur.fetchall()

    for arq_dados in rows:
        tmp_dir = BASE_DIR + os.sep + 'tmp' + os.sep
        arq_ftp = arq_dados['caminho'] + arq_dados['nome']
        dbc_local = tmp_dir + arq_dados['nome']
        dbf_local = tmp_dir + arq_dados['nome'][:-3]+'dbf'

        ftp = FtpClient('ftp.datasus.gov.br', 'anonymous', 'tabwin@tabwin.com.br')
        ftp.download(arq_ftp, dbc_local)

        data_hora = datetime.datetime.now()
        hash_md5 = md5_arquivo(dbc_local)
        upd = "update arquivo_dados set hash_md5 = %s, dt_importacao = %s where id = %s"
        cur.execute(upd, (hash_md5, data_hora, arq_dados['id']))

        expandedbc = dbc2dbf(dbc_local, tmp_dir)
        if (expandedbc == 0):
            print('Importando arquivo {} '.format(dbf_local,))
            cur.execute("delete from dados.dados_sia where id_arqdados = %s", (arq_dados['id'],))
            qtd = importaDbf(conn, dbf_local, 'dados_sia', arq_dados['id'])
            print('Inseridos: {} registros'.format(qtd,))

        os.remove(dbc_local)
        os.remove(dbf_local)
        conn.commit()

    cur.close()
    conn.close()

def gera_resumo(estado, ano, mes):
    print("Gerando Resumo SIA de {} do mes {} ano {}".format(estado, mes, ano))

    conn = db.get_conn()
    cur = conn.cursor()

    sql = "select * from arquivo_dados where tipo = 'SIA' and sub_tipo = 'PA' and ano = %s order by estado, ano, mes"
    cur.execute(sql, (ano,))

    rows = cur.fetchall()

    for arq_dados in rows:

        diretorio = '/dados/sqlite/sia/'
        #diretorio = 'C:\\Projetos\\infoSUS\\tmp\\'
        base_sqlite = diretorio + arq_dados['nome'][:-4] + '.db'

        conn_sq = sqlite3.connect(base_sqlite)
        conn_sq.execute('PRAGMA synchronous = OFF')
        conn_sq.execute('PRAGMA journal_mode = MEMORY')
        cur_sq = conn_sq.execute("""select  pa_mvm,
                        pa_ufmun,
                        pa_cnpjmnt,
                        pa_cnpjcpf,
                        pa_coduni,
                        pa_tpups,
                        pa_tippre,
                        pa_docorig,
                        sum(pa_qtdapr) pa_qtdapr,
                        sum(pa_valapr) pa_valapr,
                        sum(pa_qtdpro) pa_qtdpro,
                        sum(pa_valpro) pa_valpro,
                        sum(pa_vl_cf) pa_vl_cf,
                        sum(pa_vl_cl) pa_vl_cl,
                        sum(pa_vl_inc) pa_vl_inc,
                        sum(pa_dif_val) pa_dif_val
                from    sia
                group by pa_mvm, pa_ufmun, pa_cnpjmnt, pa_cnpjcpf, pa_coduni, pa_tpups, pa_tippre, pa_docorig
                order by 1,2,3,4,5,6,7,8""")

        for res in cur_sq:
            sql_ins = """INSERT INTO dados.sia_resumo (id_arqdados,dt_cmpt,pa_mvm,pa_ufmun,pa_cnpjmnt,pa_cnpjcpf,pa_coduni,pa_tpups,pa_tippre,pa_docorig,pa_qtdapr,pa_valapr,pa_qtdpro,pa_valpro,pa_vl_cf,pa_vl_cl,pa_vl_inc,pa_dif_val)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cur.execute(sql_ins, (arq_dados['id'],
                                    res[0][:4] + '-' + res[0][4:6] + '-01',
                                    res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[9],res[10],res[11],res[12],res[13],res[14],res[15]))
        conn.commit()
        print('OK - Resumo do arquivo {} '.format(base_sqlite,))
        #print('Inseridos: {} registros'.format(qtd,))
        conn_sq.close()

    cur.close()
    conn.close()
