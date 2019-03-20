#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Python source code - replace this with a description of the code and write the code below this text.
"""

import psycopg2
import psycopg2.extras
import cnes

try:
    conn = psycopg2.connect("host=localhost dbname=siteatw user=postgres password=secret")
except:
    print("Erro na conexao com o Banco de Dados")

try:
    arq = open('estabelecimentos.txt', 'w')
except:
    print("Nao foi possivel criar o arquivo %s" % arquivo)

cur_insert = conn.cursor()
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

sql_insert = """INSERT INTO estab_cnes_resumo(
            codcnes, nome, cnpj, gestao, municipio_id)
                VALUES (%s, %s, %s, %s, %s)"""

cur.execute("select id::text, codibge::text as municipio, estado_id::text as estado, nome from municipio where id not in (SELECT distinct municipio_id FROM estab_cnes_resumo) order by id")
muns = cur.fetchall()

for mun in muns:
    print mun['nome']
    for estab in cnes.busca_estab_mun(mun['estado'], mun['municipio'][0:6]):
        arq.write(mun['id'] + '|' + estab['cnes'] + '|' + estab['cnpj'] + '|' + estab['nome'] + '|' + estab['gestao'] + '\n')
        cur_insert.execute(sql_insert, (estab['cnes'], estab['nome'], estab['cnpj'], estab['gestao'], mun['id']))
    conn.commit()

cur.close()
conn.close()
arq.close()
