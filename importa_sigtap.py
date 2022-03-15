#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
import os
import comandos
import psycopg2
# import sqlite3
# import comandos_sqlite as comandos

funcao_insere = {'tb_procedimento': comandos.ins_procedimento,
                'tb_grupo': comandos.ins_grupo,
                'tb_sub_grupo': comandos.ins_sub_grupo,
                'tb_forma_organizacao': comandos.ins_forma_organizacao,
                'tb_cid': comandos.ins_cid,
                'tb_descricao': comandos.ins_descricao,
                'tb_descricao_detalhe': comandos.ins_descricao_detalhe,
                'tb_detalhe': comandos.ins_detalhe,
                'tb_financiamento': comandos.ins_financiamento,
                'tb_grupo_habilitacao': comandos.ins_grupo_habilitacao,
                'tb_habilitacao': comandos.ins_habilitacao,
                'tb_modalidade': comandos.ins_modalidade,
                'tb_ocupacao': comandos.ins_ocupacao,
                'tb_registro': comandos.ins_registro,
                'tb_regra_condicionada': comandos.ins_regra_condicionada,
                'tb_renases': comandos.ins_renases,
                'tb_rubrica': comandos.ins_rubrica,
                'tb_servico': comandos.ins_servico,
                'tb_servico_classificacao': comandos.ins_servico_classificacao,
                'tb_sia_sih': comandos.ins_sia_sih,
                'tb_tipo_leito': comandos.ins_tipo_leito,
                'tb_componente_rede': comandos.ins_componente_rede,
                'tb_rede_atencao': comandos.ins_rede_atencao,
                'tb_tuss': comandos.ins_tuss,
                'rl_excecao_compatibilidade': comandos.ins_rl_excecao_compatibilidade,
                'rl_procedimento_cid': comandos.ins_rl_procedimento_cid,
                'rl_procedimento_compativel': comandos.ins_rl_procedimento_compativel,
                'rl_procedimento_comp_rede': comandos.ins_rl_procedimento_comp_rede,
                'rl_procedimento_detalhe': comandos.ins_rl_procedimento_detalhe,
                'rl_procedimento_habilitacao': comandos.ins_rl_procedimento_habilitacao,
                'rl_procedimento_incremento': comandos.ins_rl_procedimento_incremento,
                'rl_procedimento_leito': comandos.ins_rl_procedimento_leito,
                'rl_procedimento_modalidade': comandos.ins_rl_procedimento_modalidade,
                'rl_procedimento_ocupacao': comandos.ins_rl_procedimento_ocupacao,
                'rl_procedimento_origem': comandos.ins_rl_procedimento_origem,
                'rl_procedimento_registro': comandos.ins_rl_procedimento_registro,
                'rl_procedimento_regra_cond': comandos.ins_rl_procedimento_regra_cond,
                'rl_procedimento_renases': comandos.ins_rl_procedimento_renases,
                'rl_procedimento_servico': comandos.ins_rl_procedimento_servico,
                'rl_procedimento_sia_sih': comandos.ins_rl_procedimento_sia_sih}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(
            'Informe o diretorio do arquivos como argumento na linha de comando.')

    diretorio = sys.argv[1]

    try:
        conn = psycopg2.connect(
            "host=localhost dbname=sigtap user=sigtap password=sigtap")
        #conn = sqlite3.connect('sigtap.db')
    except psycopg2.Error as ex:
        print("Erro na conexão com o Banco de Dados")

    arquivos = [f for f in os.listdir(diretorio) if any(f.endswith(ext) for ext in ['txt'])]

    for arquivo in arquivos:

        print("Importando o arquivo: " + arquivo)

        try:
            entrada = open(diretorio + os.path.sep + arquivo, 'r')
        except IOError as ex:
            print("Não foi possivel abrir o arquivo %s" % arquivo)

        cur = conn.cursor()
        # cur.execute("set search_path to sigtap")

        tabela = os.path.splitext(os.path.basename(arquivo))[0]

        cur.execute("delete from " + tabela)

        for linha in entrada.readlines():
            cur.execute(funcao_insere[tabela](linha)[
                        0], funcao_insere[tabela](linha)[1])

        conn.commit()
        cur.close()

    conn.close()
