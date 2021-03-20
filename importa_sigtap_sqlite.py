#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
import os
import sqlite3
import comandos_sqlite as comandos

funcao_insere = {'tb_procedimento': comandos.ins_procedimento,
                'tb_grupo': comandos.ins_grupo,
                'tb_sub_grupo': comandos.ins_sub_grupo,
                'tb_forma_organizacao': comandos.ins_forma_organizacao,
                'tb_cid': comandos.ins_cid,
                'tb_descricao': comandos.ins_descricao,
                'tb_descricao_detalhe': comandos.ins_descricao_detalhe,
                'tb_detalhe': comandos.ins_detalhe,
                'tb_componente_rede': comandos.ins_componente_rede,
                'tb_financiamento': comandos.ins_financiamento,
                'tb_grupo_habilitacao': comandos.ins_grupo_habilitacao,
                'tb_habilitacao': comandos.ins_habilitacao,
                'tb_modalidade': comandos.ins_modalidade,
                'tb_ocupacao': comandos.ins_ocupacao,
                'tb_registro': comandos.ins_registro,
                'tb_regra_condicionada': comandos.ins_regra_condicionada,
                'tb_rubrica': comandos.ins_rubrica,
                'tb_servico': comandos.ins_servico,
                'tb_servico_classificacao': comandos.ins_servico_classificacao,
                'tb_sia_sih': comandos.ins_sia_sih,
                'tb_tipo_leito': comandos.ins_tipo_leito,
                'tb_rede_atencao': comandos.ins_rede_atencao,
                'tb_renases': comandos.ins_renases,
                'tb_tuss': comandos.ins_tuss,
                'rl_excecao_compatibilidade': comandos.ins_rl_excecao_compatibilidade,
                'rl_procedimento_cid': comandos.ins_rl_procedimento_cid,
                'rl_procedimento_compativel': comandos.ins_rl_procedimento_compativel,
                'rl_procedimento_detalhe': comandos.ins_rl_procedimento_detalhe,
                'rl_procedimento_habilitacao': comandos.ins_rl_procedimento_habilitacao,
                'rl_procedimento_incremento': comandos.ins_rl_procedimento_incremento,
                'rl_procedimento_leito': comandos.ins_rl_procedimento_leito,
                'rl_procedimento_modalidade': comandos.ins_rl_procedimento_modalidade,
                'rl_procedimento_ocupacao': comandos.ins_rl_procedimento_ocupacao,
                'rl_procedimento_origem': comandos.ins_rl_procedimento_origem,
                'rl_procedimento_registro': comandos.ins_rl_procedimento_registro,
                'rl_procedimento_regra_cond': comandos.ins_rl_procedimento_regra_cond,
                'rl_procedimento_servico': comandos.ins_rl_procedimento_servico,
                'rl_procedimento_sia_sih': comandos.ins_rl_procedimento_sia_sih,
                'rl_procedimento_comp_rede': comandos.ins_rl_procedimento_comp_rede,
                'rl_procedimento_renases': comandos.ins_rl_procedimento_renases,
                }


sql_create_tables = """create table rl_excecao_compatibilidade (
    CO_PROCEDIMENTO_RESTRICAO VARCHAR(10),
    CO_PROCEDIMENTO_PRINCIPAL VARCHAR(10),
    CO_REGISTRO_PRINCIPAL VARCHAR(2),
    CO_PROCEDIMENTO_COMPATIVEL VARCHAR(10),
    CO_REGISTRO_COMPATIVEL VARCHAR(2),
    TP_COMPATIBILIDADE VARCHAR(1),
    DT_COMPETENCIA CHAR(6)
);

create table rl_procedimento_cid (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_CID VARCHAR(4),
    ST_PRINCIPAL CHAR(1),
    DT_COMPETENCIA CHAR(6)
);

create table rl_procedimento_compativel (
    CO_PROCEDIMENTO_PRINCIPAL VARCHAR(10),
    CO_REGISTRO_PRINCIPAL VARCHAR(2),
    CO_PROCEDIMENTO_COMPATIVEL VARCHAR(10),
    CO_REGISTRO_COMPATIVEL VARCHAR(2),
    TP_COMPATIBILIDADE VARCHAR(1),
    QT_PERMITIDA NUMBER(4),
    DT_COMPETENCIA CHAR(6)
);

create table rl_procedimento_comp_rede (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_COMPONENTE_REDE VARCHAR(10)
);

create table rl_procedimento_detalhe (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_DETALHE VARCHAR(3),
    DT_COMPETENCIA CHAR(6)
);

create table rl_procedimento_habilitacao (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_HABILITACAO VARCHAR(4),
    NU_GRUPO_HABILITACAO VARCHAR(4),
    DT_COMPETENCIA CHAR(6)
);

create table rl_procedimento_incremento (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_HABILITACAO VARCHAR(4),
    VL_PERCENTUAL_SH NUMBER(7),
    VL_PERCENTUAL_SA NUMBER(7),
    VL_PERCENTUAL_SP NUMBER(7),
    DT_COMPETENCIA CHAR(6)
);

create table rl_procedimento_leito (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_TIPO_LEITO VARCHAR(2),
    DT_COMPETENCIA CHAR(6)
);

create table rl_procedimento_modalidade (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_MODALIDADE VARCHAR(2),
    DT_COMPETENCIA CHAR(6)
);

create table rl_procedimento_ocupacao (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_OCUPACAO CHAR(6),
    DT_COMPETENCIA CHAR(6)
);

create table rl_procedimento_origem (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_PROCEDIMENTO_ORIGEM VARCHAR(10),
    DT_COMPETENCIA CHAR(6)
);

create table rl_procedimento_registro (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_REGISTRO VARCHAR(2),
    DT_COMPETENCIA CHAR(6)
);

create table rl_procedimento_regra_cond (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_REGRA_CONDICIONADA VARCHAR(4)
);

create table rl_procedimento_renases (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_RENASES VARCHAR(10)
);

create table rl_procedimento_servico (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_SERVICO VARCHAR(3),
    CO_CLASSIFICACAO VARCHAR(3),
    DT_COMPETENCIA CHAR(6)
);

create table rl_procedimento_sia_sih (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_PROCEDIMENTO_SIA_SIH VARCHAR(10),
    TP_PROCEDIMENTO VARCHAR(1),
    DT_COMPETENCIA CHAR(6)
);

create table rl_procedimento_tuss (
    CO_PROCEDIMENTO VARCHAR(10),
    CO_TUSS VARCHAR(10)
);

create table tb_cid (
    CO_CID VARCHAR(4),
    NO_CID VARCHAR(100),
    TP_AGRAVO CHAR(1),
    TP_SEXO CHAR(1),
    TP_ESTADIO CHAR(1),
    VL_CAMPOS_IRRADIADOS NUMBER(4)
);

create table tb_componente_rede (
    CO_COMPONENTE_REDE VARCHAR(10),
    NO_COMPONENTE_REDE VARCHAR(150),
    CO_REDE_ATENCAO VARCHAR(3)
);

create table tb_descricao_detalhe (
    CO_DETALHE VARCHAR(3),
    DS_DETALHE VARCHAR(4000),
    DT_COMPETENCIA CHAR(6)
);

create table tb_descricao (
    CO_PROCEDIMENTO VARCHAR(10),
    DS_PROCEDIMENTO VARCHAR(4000),
    DT_COMPETENCIA CHAR(6)
);

create table tb_detalhe (
    CO_DETALHE VARCHAR(3),
    NO_DETALHE VARCHAR(100),
    DT_COMPETENCIA CHAR(6)
);

create table tb_financiamento (
    CO_FINANCIAMENTO VARCHAR(2),
    NO_FINANCIAMENTO VARCHAR(100),
    DT_COMPETENCIA CHAR(6)
);

create table tb_forma_organizacao (
    CO_GRUPO VARCHAR(2),
    CO_SUB_GRUPO VARCHAR(2),
    CO_FORMA_ORGANIZACAO VARCHAR(2),
    NO_FORMA_ORGANIZACAO VARCHAR(100),
    DT_COMPETENCIA CHAR(6)
);

create table tb_grupo_habilitacao (
    NU_GRUPO_HABILITACAO VARCHAR(4),
    NO_GRUPO_HABILITACAO VARCHAR(20),
    DS_GRUPO_HABILITACAO VARCHAR(250)
);

create table tb_grupo (
    CO_GRUPO VARCHAR(2),
    NO_GRUPO VARCHAR(100),
    DT_COMPETENCIA CHAR(6)
);

create table tb_habilitacao (
    CO_HABILITACAO VARCHAR(4),
    NO_HABILITACAO VARCHAR(150),
    DT_COMPETENCIA CHAR(6)
);

create table tb_modalidade (
    CO_MODALIDADE VARCHAR(2),
    NO_MODALIDADE VARCHAR(100),
    DT_COMPETENCIA CHAR(6)
);

create table tb_ocupacao (
    CO_OCUPACAO CHAR(6),
    NO_OCUPACAO VARCHAR(150)
);

create table tb_procedimento (
    CO_PROCEDIMENTO VARCHAR(10),
    NO_PROCEDIMENTO VARCHAR(250),
    TP_COMPLEXIDADE VARCHAR(1),
    TP_SEXO VARCHAR(1),
    QT_MAXIMA_EXECUCAO NUMBER(4),
    QT_DIAS_PERMANENCIA NUMBER(4),
    QT_PONTOS NUMBER(4),
    VL_IDADE_MINIMA NUMBER(4),
    VL_IDADE_MAXIMA NUMBER(4),
    VL_SH NUMBER(10),
    VL_SA NUMBER(10),
    VL_SP NUMBER(10),
    CO_FINANCIAMENTO VARCHAR(2),
    CO_RUBRICA VARCHAR(6),
    QT_TEMPO_PERMANENCIA NUMBER(4),
    DT_COMPETENCIA CHAR(6)
);

create table tb_rede_atencao (
    CO_REDE_ATENCAO VARCHAR(3),
    NO_REDE_ATENCAO VARCHAR(50)
);

create table tb_registro (
    CO_REGISTRO VARCHAR(2),
    NO_REGISTRO VARCHAR(50),
    DT_COMPETENCIA CHAR(6)
);

create table tb_regra_condicionada (
    CO_REGRA_CONDICIONADA VARCHAR(4),
    NO_REGRA_CONDICIONADA VARCHAR(150),
    DS_REGRA_CONDICIONADA VARCHAR(4000)
);

create table tb_renases (
    CO_RENASES VARCHAR(10),
    NO_RENASES VARCHAR(150)
);

create table tb_rubrica (
    CO_RUBRICA VARCHAR(6),
    NO_RUBRICA VARCHAR(100),
    DT_COMPETENCIA CHAR(6)
);

create table tb_servico_classificacao (
    CO_SERVICO VARCHAR(3),
    CO_CLASSIFICACAO VARCHAR(3),
    NO_CLASSIFICACAO VARCHAR(150),
    DT_COMPETENCIA CHAR(6)
);

create table tb_servico (
    CO_SERVICO VARCHAR(3),
    NO_SERVICO VARCHAR(120),
    DT_COMPETENCIA CHAR(6)
);

create table tb_sia_sih (
    CO_PROCEDIMENTO_SIA_SIH VARCHAR(10),
    NO_PROCEDIMENTO_SIA_SIH VARCHAR(100),
    TP_PROCEDIMENTO VARCHAR(1),
    DT_COMPETENCIA CHAR(6)
);

create table tb_sub_grupo (
    CO_GRUPO VARCHAR(2),
    CO_SUB_GRUPO VARCHAR(2),
    NO_SUB_GRUPO VARCHAR(100),
    DT_COMPETENCIA CHAR(6)
);

create table tb_tipo_leito (
    CO_TIPO_LEITO VARCHAR(2),
    NO_TIPO_LEITO VARCHAR(60),
    DT_COMPETENCIA CHAR(6)
);

create table tb_tuss (
    CO_TUSS VARCHAR(10),
    NO_TUSS VARCHAR(450)
);"""

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(
            'Informe o diretorio do arquivos como argumento na linha de comando.')

    diretorio = sys.argv[1]
    base_sqllite = sys.argv[2]

    try:
        conn = sqlite3.connect(base_sqllite)
    except sqlite3.Error as ex:
        print("Erro na conexão com o Banco de Dados")

    conn.executescript(sql_create_tables)
    conn.commit()

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
        print("Excluindo registros da tabela %s" % tabela)
        cur.execute("delete from " + tabela)

        for linha in entrada.readlines():
            cur.execute(funcao_insere[tabela](linha)[
                0], funcao_insere[tabela](linha)[1])

        conn.commit()
        cur.close()

    conn.close()
