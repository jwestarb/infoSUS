#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Importa Estabelecimento do site cnes.datasus.gov.br
"""
import psycopg2
import psycopg2.extras
import estab_cnes

try:
    conn = psycopg2.connect("host=localhost dbname=siteatw user=postgres password=secret")
except:
    print("Erro na conexao com o Banco de Dados")

print('Buscando Estabelecimento da tabela de resumo...')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
sql = """
SELECT  a.codcnes codcnes, a.nome nome, a.cnpj cnpj, a.gestao gestao, b.nome municipio ,b.id id_municipio, b.codibge::text codibge, c.sigla sg_estado, c.nome estado
FROM    estab_cnes_resumo a, 
        municipio b, 
        estado c
where   a.municipio_id = b.id
and     b.estado_id = c.id
and     a.dt_atualizacao is null
order   by a.codcnes
"""

cur.execute(sql)
rows = cur.fetchall()

i = 0
for row in rows:
    i = i + 1
    print('[' + str(i) + '] Buscando Estabelecimento: ' + row['nome'])
    estab = estab_cnes.busca_estab(str(row['codcnes']), row['codibge'][:6])
    if (len(estab) == 22):
        cur_insert = conn.cursor()
        sql_insert = """INSERT INTO estab_cnes(
        id, bairro, cep, cnpj, cnpjmantenedora, codibgesemdv, codcnes,
        complemento, cpf, dependencia, email, esferaadm, fax, gestaoextenso,
        logradouro, naturezaorg, nome, numero, personalidade, razaosocial,
        regiaosaude, subtipoestab, telefone, terceiros, tipoestab, tipogestao, municipio_id)
        VALUES (nextval('estab_cnes_id_seq'), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        params = (estab['bairro'], estab['cep'], estab['cnpj'], estab['cnpjMantenedora'], row['codibge'][:6], row['codcnes'], estab['complemento'], estab['cpf'], estab['dependencia'], estab['email'], estab['esferaAdm'], estab['fax'], estab['gestaoExtenso'], estab['logradouro'], estab['naturezaOrg'], estab['nome'], estab['numero'], estab['personalidade'], estab['razaoSocial'], estab['regiaoSaude'], estab['subTipoEstab'], estab['telefone'], estab['terceiros'], estab['tipoEstab'], row['gestao'], row['id_municipio'])
        cur_insert.execute(sql_insert, params)

        cur_update = conn.cursor()
        sql_update = "update estab_cnes_resumo set dt_atualizacao = LOCALTIMESTAMP where codcnes = %s"
        cur_update.execute(sql_update, (row['codcnes'],))

        conn.commit()
        cur_insert.close()
        cur_update.close()

cur.close()
conn.close()
