#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Importa os arquivos DBF para o SqLite
"""
import os
import time
import sqlite3
from dbfpy3 import dbf

def dbfsia2sqlite(arquivo, nome_arq):
    diretorio = '/dados/sqlite/sia/'
    base_sqlite = nome_arq[:-4]
    os.remove(diretorio + base_sqlite + '.db')

    conn = sqlite3.connect(diretorio + base_sqlite + '.db')
    conn.execute('PRAGMA synchronous = OFF')
    conn.execute('PRAGMA journal_mode = MEMORY')
    conn.execute('DROP TABLE IF EXISTS sia')
    conn.execute("""CREATE TABLE IF NOT EXISTS sia(
        pa_coduni varchar(7),
        pa_gestao varchar(6),
        pa_condic varchar(2),
        pa_ufmun varchar(6),
        pa_regct varchar(4),
        pa_incout varchar(4),
        pa_incurg varchar(4),
        pa_tpups varchar(2),
        pa_tippre varchar(2),
        pa_mn_ind varchar(1),
        pa_cnpjcpf varchar(14),
        pa_cnpjmnt varchar(14),
        pa_cnpj_cc varchar(14),
        pa_mvm varchar(6),
        pa_cmp varchar(6),
        pa_proc_id varchar(10),
        pa_tpfin varchar(2),
        pa_subfin varchar(4),
        pa_nivcpl varchar(1),
        pa_docorig varchar(1),
        pa_autoriz varchar(13),
        pa_cnsmed varchar(15),
        pa_cbocod varchar(6),
        pa_motsai varchar(2),
        pa_obito varchar(1),
        pa_encerr varchar(1),
        pa_perman varchar(1),
        pa_alta varchar(1),
        pa_transf varchar(1),
        pa_cidpri varchar(4),
        pa_cidsec varchar(4),
        pa_cidcas varchar(4),
        pa_catend varchar(2),
        pa_idade varchar(3),
        idademin varchar(3),
        idademax varchar(3),
        pa_flidade varchar(1),
        pa_sexo varchar(1),
        pa_racacor varchar(2),
        pa_munpcn varchar(6),
        pa_qtdpro numeric(11,0),
        pa_qtdapr numeric(11,0),
        pa_valpro numeric(20,2),
        pa_valapr numeric(20,2),
        pa_ufdif varchar(1),
        pa_mndif varchar(1),
        pa_dif_val numeric(20,2),
        nu_vpa_tot numeric(20,2),
        nu_pa_tot numeric(20,2),
        pa_indica varchar(1),
        pa_codoco varchar(1),
        pa_flqt varchar(1),
        pa_fler varchar(1),
        pa_etnia varchar(4),
        pa_vl_cf numeric(20,2),
        pa_vl_cl numeric(20,2),
        pa_vl_inc numeric(20,2),
        pa_srv_c varchar(6)
      );""")

    db = dbf.Dbf(arquivo)
    num_reg = db.recordCount

    colunas = ", ".join(db.fieldNames)
    val = ", ".join('?' for v in db.fieldNames)
    sql = "insert into sia (" + colunas + ") values (" + val + ")"

    for rec in db:
        valores = tuple(v for v in rec)
        conn.execute(sql, valores)

    conn.commit()
    conn.close()
    db.close()
    return num_reg

if __name__ == '__main__':
    ini = time.time()
    qtd = dbfsia2sqlite('PASC1411.dbf')
    fim = time.time()
    print("sia2sqlite -> Qtd Registros: {} / Tempo : {} seg".format(qtd, fim - ini))
