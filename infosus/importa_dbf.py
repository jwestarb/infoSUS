#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Importa os arquivos DBF para o Postgresql
"""
#import os
import time
import io
import shutil
import psycopg2
from dbfpy3 import dbf

def importaDbf(conn_pg, arquivo, tabela, id_arqdados):
    cur = conn_pg.cursor()

    db = dbf.Dbf(arquivo)

    qtd = db.recordCount
    colunas = ", ".join(db.fieldNames)
    val = ", ".join('%s' for v in db.fieldNames)
    sql = "insert into dados." + tabela + " (" + colunas + ", id_arqdados) values (" + val + ", " + str(id_arqdados) + ")"

    for rec in db:
        valores = tuple(v for v in rec)
        cur.execute(sql, valores)

    cur.close()
    db.close()
    return qtd

def importaDbfCopy(conn_pg, arquivo):
    cur = conn_pg.cursor()
    cur.execute("set search_path to dados")

    db = dbf.Dbf(arquivo)

    f = io.StringIO("")
    for rec in db:
        #for fldName in db.fieldNames:
            #f.write(str(rec[fldName]) + '\t')
        f.write("\t".join(str(rec[fldName]) for fldName in db.fieldNames))
        f.write('\n')

    f.seek(0)
    cur.copy_from(f, 'dados.dados_sih', sep='\t', size=8192)

    conn_pg.commit()
    cur.close()
    db.close()


def exportaDbfCsv(arquivo, saida):
    db = dbf.Dbf(arquivo)

    f = io.StringIO("")
    f.write("\t".join(db.fieldNames))
    for rec in db:
        #for fldName in db.fieldNames:
            #f.write(str(rec[fldName]) + '\t')
        f.write("\t".join(str(rec[fldName]) for fldName in db.fieldNames))
        f.write('\n')

    f.seek(0)
    saida = open(saida, 'w')
    shutil.copyfileobj(f, saida)

    saida.close()
    db.close()


if __name__ == '__main__':
    try:
        poll = psycopg2.pool.SimpleConnectionPool(2, 5, "host=192.168.100.2 dbname=siteatw user=postgres password=secret")
        #conn = psycopg2.connect("host=192.168.100.2 dbname=siteatw user=postgres password=secret")
    except psycopg2.Error as e:
        print("Erro na conexão com o Banco de Dados: " + e.pgerror)

    conn = poll.getconn()

    ini = time.time()

    importaDbf(conn, 'RDSC1411.dbf', 'dados_sih', 26177)

    fim = time.time()
    print("Tempo importaDbf: {} seg".format(fim - ini))

    poll.putconn(conn)
    poll.closeall()
