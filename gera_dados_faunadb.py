import sys
import os
import json
import psycopg2
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient


def gera_json_procedimentos(conn_pg):
    cur = conn_pg.cursor()
    cur_proc = conn_pg.cursor()

    cur.execute("select co_procedimento from tb_procedimento order by co_procedimento")
    # where co_procedimento = '0505020092'

    rows = cur.fetchall()

    for row in rows:
        print('Enviando procedimento {}'.format(row[0]))
        sql = """select array_to_json(array_agg(row_to_json(t)))
                from (
                select    a.co_procedimento co_procedimento,
                    substr(a.co_procedimento,1,2) || '.' ||
                    substr(a.co_procedimento,3,2) || '.' ||
                    substr(a.co_procedimento,5,2) || '.' ||
                    substr(a.co_procedimento,7,3) || '-' ||
                    substr(a.co_procedimento,10,1) co_proc_formatado,
                    initcap(a.no_procedimento) no_procedimento,
                    desc_complexidade(a.tp_complexidade) ds_complexidade,
                    desc_sexo(a.tp_sexo) ds_sexo,
                    CASE WHEN a.qt_maxima_execucao::text = '9999' THEN 'Não se aplica' ELSE a.qt_maxima_execucao::text END,
                    CASE WHEN a.qt_dias_permanencia::text = '9999' THEN 'Não se aplica' ELSE a.qt_dias_permanencia::text END,
                    a.qt_pontos,
                    trunc(a.vl_idade_minima/12) || ' Anos' vl_idade_minima,
                    trunc(a.vl_idade_maxima/12) || ' Anos' vl_idade_maxima,
                    a.vl_sh::money,
                    a.vl_sa::money,
                    a.vl_sp::money,
                    desc_financiamento(a.co_financiamento) ds_financiamento,
                    COALESCE(r.no_rubrica, 'Não se aplica') no_rubrica,
                    CASE WHEN a.qt_tempo_permanencia::text = '9999' THEN 'Não se aplica' ELSE a.qt_tempo_permanencia::text END,
                    ( select  array_to_json ( array_agg ( row_to_json ( r )))
                        from  (
                            select tr.no_registro
                            from rl_procedimento_registro pr,
                                tb_registro tr
                            where pr.co_registro = tr.co_registro
                            and pr.co_procedimento = a.co_procedimento
                            order by tr.co_registro ) r ) as tp_registros,
                    (select  array_to_json ( array_agg ( row_to_json ( cidp )))
                        from  (
                            select tc.co_cid, tc.no_cid
                        from rl_procedimento_cid pc,
                            tb_cid tc
                        where pc.co_cid = tc.co_cid
                        and pc.co_procedimento = a.co_procedimento
                        and pc.st_principal = 'S'
                        order by tc.co_cid ) cidp ) as cids_pri,
                    (select  array_to_json ( array_agg ( row_to_json ( cids )))
                        from  (
                            select tcs.co_cid, tcs.no_cid
                        from rl_procedimento_cid pcs,
                            tb_cid tcs
                        where pcs.co_cid = tcs.co_cid
                        and pcs.co_procedimento = a.co_procedimento
                        and pcs.st_principal = 'N'
                        order by tcs.co_cid ) cids ) as cids_sec,
                    (select  array_to_json ( array_agg ( row_to_json ( cbo )))
                        from  (
                            select tcbo.co_ocupacao, tcbo.no_ocupacao
                        from rl_procedimento_ocupacao rlcbo,
                            tb_ocupacao tcbo
                        where rlcbo.co_ocupacao = tcbo.co_ocupacao
                        and rlcbo.co_procedimento = a.co_procedimento
                        order by tcbo.co_ocupacao ) cbo ) as cbo,
                    (select  array_to_json ( array_agg ( row_to_json ( hab )))
                        from  (
                            select thab.co_habilitacao, thab.no_habilitacao
                        from rl_procedimento_habilitacao rlhab,
                            tb_habilitacao thab
                        where rlhab.co_habilitacao = thab.co_habilitacao
                        and rlhab.co_procedimento = a.co_procedimento
                        order by thab.co_habilitacao ) hab ) as habi
                FROM    tb_procedimento a
                LEFT OUTER JOIN tb_rubrica r ON r.co_rubrica = a.co_rubrica
                where   a.co_procedimento = %s
                ) t"""

        params = (row[0],)
        cur_proc.execute(sql, params)

        
        proc_json = cur_proc.fetchone()[0]
        doc  = client.query(q.create('tb_procedimento', {"data": proc_json[0]}))

    cur.close()
    cur_proc.close()


def gera_resumo_procedimentos(conn_pg, dir_saida):
    cur = conn_pg.cursor()

    sql = """select array_to_json(array_agg(row_to_json(t)))
            from (
            select    substr(a.co_procedimento,1,2) co_grupo,
                substr(a.co_procedimento,3,2) co_sub_grupo,
                substr(a.co_procedimento,5,2) co_forma_organizacao,
                a.co_procedimento co_procedimento,
                substr(a.co_procedimento,1,2) || '.' ||
                substr(a.co_procedimento,3,2) || '.' ||
                substr(a.co_procedimento,5,2) || '.' ||
                substr(a.co_procedimento,7,3) || '-' ||
                substr(a.co_procedimento,10,1) co_proc_formatado,
                initcap(a.no_procedimento) no_procedimento
            from     tb_procedimento a
            ) t"""

    cur.execute(sql)

    arquivo = dir_saida + os.path.sep + 'procedimentos.json'

    try:
        arq = open(arquivo, 'w', encoding='utf-8')
    except IOError:
        print("Não foi possivel criar o arquivo %s" % arquivo)

    json.dump(cur.fetchone()[0], arq, ensure_ascii=False, sort_keys=True)

    arq.close()
    cur.close()


def gera_grupos(conn_pg, dir_saida):
    cur = conn_pg.cursor()

    sql = """select array_to_json(array_agg(row_to_json(t)))
			from (
			    select co_grupo, no_grupo,
			    (
			      select  array_to_json ( array_agg ( row_to_json ( d )))
			      from  (
			        select co_grupo, co_sub_grupo, no_sub_grupo,
			        (
			        select  array_to_json ( array_agg ( row_to_json ( f )))
			        from  (
			         select co_grupo, co_sub_grupo, co_forma_organizacao, no_forma_organizacao
			         from tb_forma_organizacao c
			         where c.co_sub_grupo = b.co_sub_grupo
			         and c.co_grupo = b.co_grupo ) f
			        ) as formas_organizacao
			        from  tb_sub_grupo b
			        where  a.co_grupo = b.co_grupo
			      )  d
			    )  as  sub_grupos
			    from tb_grupo a
			) t"""

    cur.execute(sql)

    arquivo = dir_saida + os.path.sep + 'grupos.json'

    try:
        arq = open(arquivo, 'w', encoding='utf-8')
    except IOError:
        print("Não foi possivel criar o arquivo %s" % arquivo)

    json.dump(cur.fetchone()[0], arq, ensure_ascii=False, sort_keys=True)

    arq.close()
    cur.close()


if __name__ == '__main__':
    client = FaunaClient(secret='fnAEExm8DfACCRQ3ZqKHFlMjM-0cU59pNo7UDkAW')

    if len(sys.argv) < 1:
        raise SystemExit(
            'Informe o comando.')

    comando = sys.argv[1]

    try:
        conn = psycopg2.connect(
            "host=localhost dbname=sigtap user=sigtap password=sigtap")
    except psycopg2.Error as ex:
        print("Erro na conexão com o Banco de Dados")

    if comando == 'grupos':
        gera_grupos(conn, diretorio)

    if comando == 'resumo':
        gera_resumo_procedimentos(conn, diretorio)

    if comando == 'procedimentos':
        gera_json_procedimentos(conn)

    conn.close()
