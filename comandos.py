#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def ins_grupo(linha):
    comando = """insert into tb_grupo (
                    CO_GRUPO,
                    NO_GRUPO,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:2].strip(), linha[2:102].strip(), linha[102:108])
    return comando, dados

def ins_sub_grupo(linha):
    comando = """insert into tb_sub_grupo (
                    CO_GRUPO,
                    CO_SUB_GRUPO,
                    NO_SUB_GRUPO,
                    DT_COMPETENCIA)
                values (%s,%s,%s,%s)"""
    dados = (linha[0:2].strip(), linha[2:4].strip(), linha[4:104].strip(), linha[104:110])
    return comando, dados

def ins_forma_organizacao(linha):
    comando = """insert into tb_forma_organizacao (
                    CO_GRUPO,
                    CO_SUB_GRUPO,
                    CO_FORMA_ORGANIZACAO,
                    NO_FORMA_ORGANIZACAO,
                    DT_COMPETENCIA)
                values (%s,%s,%s,%s,%s)"""
    dados = (linha[0:2].strip(), linha[2:4].strip(), linha[4:6].strip(), linha[6:106].strip(), linha[106:112])
    return comando, dados

def ins_procedimento(linha):
    comando = """insert into tb_procedimento (
                    CO_PROCEDIMENTO,
                    NO_PROCEDIMENTO,
                    TP_COMPLEXIDADE,
                    TP_SEXO,
                    QT_MAXIMA_EXECUCAO,
                    QT_DIAS_PERMANENCIA,
                    QT_PONTOS,
                    VL_IDADE_MINIMA,
                    VL_IDADE_MAXIMA,
                    VL_SH,VL_SA,
                    VL_SP,
                    CO_FINANCIAMENTO,
                    CO_RUBRICA,
                    QT_TEMPO_PERMANENCIA,
                    DT_COMPETENCIA)
                values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    dados = (linha[0:10],
            linha[10:260].strip(),
            linha[260:261].strip(),
            linha[261:262].strip(),
            linha[262:266].strip(),
            linha[266:270].strip(),
            linha[270:274].strip(),
            linha[274:278].strip(),
            linha[278:282].strip(),
            linha[282:290].lstrip('0') + '.' + linha[290:292],
            linha[292:300].lstrip('0') + '.' + linha[300:302],
            linha[302:310].lstrip('0') + '.' + linha[310:312],
            linha[312:314].strip(),
            linha[314:320].strip(),
            linha[320:324].strip(),
            linha[324:330])
    return comando, dados

def ins_cid(linha):
    comando = """insert into tb_cid (
                    CO_CID,
                    NO_CID,
                    TP_AGRAVO,
                    TP_SEXO,
                    TP_ESTADIO,
                    VL_CAMPOS_IRRADIADOS)
                values (%s,%s,%s,%s,%s,%s)"""
    dados = (linha[0:4].strip(), linha[4:104].strip(), linha[104:105].strip(), linha[105:106].strip(), linha[106:107].strip(), linha[107:111].strip())
    return comando, dados

def ins_descricao(linha):
    comando = """insert into tb_descricao (
                    CO_PROCEDIMENTO,
                    DS_PROCEDIMENTO,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:10], linha[10:4010].strip(), linha[4010:4016])
    return comando, dados

def ins_detalhe(linha):
    comando = """insert into tb_detalhe (
                    CO_DETALHE,
                    NO_DETALHE,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:3], linha[3:103].strip(), linha[103:109])
    return comando, dados

def ins_descricao_detalhe(linha):
    comando = """insert into tb_descricao_detalhe (
                    CO_DETALHE,
                    DS_DETALHE,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:3], linha[3:4003].strip(), linha[4003:4009])
    return comando, dados

def ins_financiamento(linha):
    comando = """insert into tb_financiamento (
                    CO_FINANCIAMENTO,
                    NO_FINANCIAMENTO,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:2], linha[2:102].strip(), linha[102:108])
    return comando, dados

def ins_grupo_habilitacao(linha):
    comando = """insert into tb_grupo_habilitacao (
                    NU_GRUPO_HABILITACAO,
                    NO_GRUPO_HABILITACAO,
                    DS_GRUPO_HABILITACAO)
                values (%s,%s,%s)"""
    dados = (linha[0:4].strip(), linha[4:24].strip(), linha[24:274].strip())
    return comando, dados

def ins_habilitacao(linha):
    comando = """insert into tb_habilitacao (
                    CO_HABILITACAO,
                    NO_HABILITACAO,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:4], linha[4:154].strip(), linha[154:160])
    return comando, dados

def ins_modalidade(linha):
    comando = """insert into tb_modalidade (
                    CO_MODALIDADE,
                    NO_MODALIDADE,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:2], linha[2:102].strip(), linha[102:108])
    return comando, dados

def ins_ocupacao(linha):
    comando = """insert into tb_ocupacao (
                    CO_OCUPACAO,
                    NO_OCUPACAO)
                values (%s,%s)"""
    dados = (linha[0:6], linha[6:156].strip())
    return comando, dados

def ins_renases(linha):
    comando = """insert into tb_renases (
                    CO_RENASES,
                    NO_RENASES)
                values (%s,%s)"""
    dados = (linha[0:10], linha[10:160].strip())
    return comando, dados

def ins_rede_atencao(linha):
    comando = """insert into tb_rede_atencao (
                    CO_REDE_ATENCAO,
                    NO_REDE_ATENCAO)
                values (%s,%s)"""
    dados = (linha[0:3], linha[3:53].strip())
    return comando, dados

def ins_tuss(linha):
    comando = """insert into tb_tuss (
                    CO_TUSS,
                    NO_TUSS)
                values (%s,%s)"""
    dados = (linha[0:10], linha[10:460].strip())
    return comando, dados

def ins_registro(linha):
    comando = """insert into tb_registro (
                    CO_REGISTRO,
                    NO_REGISTRO,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:2], linha[2:52].strip(), linha[52:58])
    return comando, dados

def ins_regra_condicionada(linha):
    comando = """insert into tb_regra_condicionada (
                    CO_REGRA_CONDICIONADA,
                    NO_REGRA_CONDICIONADA,
                    DS_REGRA_CONDICIONADA)
                values (%s,%s,%s)"""
    dados = (linha[0:4], linha[4:154].strip(), linha[154:4154].strip())
    return comando, dados

def ins_componente_rede(linha):
    comando = """insert into tb_componente_rede (
                    CO_COMPONENTE_REDE,
                    NO_COMPONENTE_REDE,
                    CO_REDE_ATENCAO)
                values (%s,%s,%s)"""
    dados = (linha[0:10], linha[10:160].strip(), linha[160:163].strip())
    return comando, dados

def ins_rubrica(linha):
    comando = """insert into tb_rubrica (
                    CO_RUBRICA,
                    NO_RUBRICA,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:6], linha[6:106].strip(), linha[106:112])
    return comando, dados



def ins_servico(linha):
    comando = """insert into tb_servico (
                    CO_SERVICO,
                    NO_SERVICO,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:3], linha[3:123].strip(), linha[123:129])
    return comando, dados

def ins_servico_classificacao(linha):
    comando = """insert into tb_servico_classificacao (
                    CO_SERVICO,
                    CO_CLASSIFICACAO,
                    NO_CLASSIFICACAO,
                    DT_COMPETENCIA)
                values (%s,%s,%s,%s)"""
    dados = (linha[0:3], linha[3:6].strip(), linha[6:156].strip(), linha[156:162])
    return comando, dados

def ins_sia_sih(linha):
    comando = """insert into tb_sia_sih (
                    CO_PROCEDIMENTO_SIA_SIH,
                    NO_PROCEDIMENTO_SIA_SIH,
                    TP_PROCEDIMENTO,
                    DT_COMPETENCIA)
                values (%s,%s,%s,%s)"""
    dados = (linha[0:10].strip(), linha[10:110].strip(), linha[110:111].strip(), linha[111:117])
    return comando, dados

def ins_tipo_leito(linha):
    comando = """insert into tb_tipo_leito (
                    CO_TIPO_LEITO,
                    NO_TIPO_LEITO,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:2], linha[2:62].strip(), linha[62:68])
    return comando, dados


def ins_rl_excecao_compatibilidade(linha):
    comando = """insert into rl_excecao_compatibilidade (
                    CO_PROCEDIMENTO_RESTRICAO,
                    CO_PROCEDIMENTO_PRINCIPAL,
                    CO_REGISTRO_PRINCIPAL,
                    CO_PROCEDIMENTO_COMPATIVEL,
                    CO_REGISTRO_COMPATIVEL,
                    TP_COMPATIBILIDADE,
                    DT_COMPETENCIA)
                values (%s,%s,%s,%s,%s,%s,%s)"""
    dados = (linha[0:10].strip(), linha[10:20].strip(), linha[20:22].strip(), linha[22:32].strip(), linha[32:34].strip(), linha[34:35].strip(), linha[35:41])
    return comando, dados

def ins_rl_procedimento_cid(linha):
    comando = """insert into rl_procedimento_cid (
                    CO_PROCEDIMENTO,
                    CO_CID,
                    ST_PRINCIPAL,
                    DT_COMPETENCIA)
                values (%s,%s,%s,%s)"""
    dados = (linha[0:10], linha[10:14].strip(), linha[14:15].strip(), linha[15:21])
    return comando, dados

def ins_rl_procedimento_compativel(linha):
    comando = """insert into rl_procedimento_compativel (
                    CO_PROCEDIMENTO_PRINCIPAL,
                    CO_REGISTRO_PRINCIPAL,
                    CO_PROCEDIMENTO_COMPATIVEL,
                    CO_REGISTRO_COMPATIVEL,
                    TP_COMPATIBILIDADE,
                    QT_PERMITIDA,
                    DT_COMPETENCIA)
                values (%s,%s,%s,%s,%s,%s,%s)"""
    dados = (linha[0:10], linha[10:12].strip(), linha[12:22].strip(), linha[22:24].strip(), linha[24:25].strip(), linha[25:29].strip(), linha[29:35])
    return comando, dados

def ins_rl_procedimento_comp_rede(linha):
    comando = """insert into rl_procedimento_comp_rede (
                    CO_PROCEDIMENTO,
                    CO_COMPONENTE_REDE)
                values (%s,%s)"""
    dados = (linha[0:10], linha[10:15].strip())
    return comando, dados

def ins_rl_procedimento_renases(linha):
    comando = """insert into rl_procedimento_renases (
                    CO_PROCEDIMENTO,
                    CO_RENASES)
                values (%s,%s)"""
    dados = (linha[0:10], linha[10:13].strip())
    return comando, dados

def ins_rl_procedimento_detalhe(linha):
    comando = """insert into rl_procedimento_detalhe (
                    CO_PROCEDIMENTO,
                    CO_DETALHE,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:10], linha[10:13].strip(), linha[13:19])
    return comando, dados

def ins_rl_procedimento_habilitacao(linha):
    comando = """insert into rl_procedimento_habilitacao (
                    CO_PROCEDIMENTO,
                    CO_HABILITACAO,
                    NU_GRUPO_HABILITACAO,
                    DT_COMPETENCIA)
                values (%s,%s,%s,%s)"""
    dados = (linha[0:10], linha[10:14].strip(), linha[14:18].strip(), linha[18:24])
    return comando, dados

def ins_rl_procedimento_incremento(linha):
    comando = """insert into rl_procedimento_incremento (
                    CO_PROCEDIMENTO,
                    CO_HABILITACAO,
                    VL_PERCENTUAL_SH,
                    VL_PERCENTUAL_SA,
                    VL_PERCENTUAL_SP,
                    DT_COMPETENCIA)
                values (%s,%s,%s,%s,%s,%s)"""
    dados = (linha[0:10],
            linha[10:14],
            linha[14:19].lstrip('0') + '.' + linha[19:21],
            linha[21:25].lstrip('0') + '.' + linha[25:28],
            linha[28:32].lstrip('0') + '.' + linha[32:35],
            linha[35:41])
    return comando, dados

def ins_rl_procedimento_leito(linha):
    comando = """insert into rl_procedimento_leito (
                    CO_PROCEDIMENTO,
                    CO_TIPO_LEITO,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:10], linha[10:12], linha[12:18])
    return comando, dados

def ins_rl_procedimento_modalidade(linha):
    comando = """insert into rl_procedimento_modalidade (
                    CO_PROCEDIMENTO,
                    CO_MODALIDADE,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:10], linha[10:12], linha[12:18])
    return comando, dados

def ins_rl_procedimento_ocupacao(linha):
    comando = """insert into rl_procedimento_ocupacao (
                    CO_PROCEDIMENTO,
                    CO_OCUPACAO,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:10], linha[10:16], linha[16:22])
    return comando, dados

def ins_rl_procedimento_origem(linha):
    comando = """insert into rl_procedimento_origem (
                    CO_PROCEDIMENTO,
                    CO_PROCEDIMENTO_ORIGEM,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:10], linha[10:20], linha[20:26])
    return comando, dados

def ins_rl_procedimento_registro(linha):
    comando = """insert into rl_procedimento_registro (
                    CO_PROCEDIMENTO,
                    CO_REGISTRO,
                    DT_COMPETENCIA)
                values (%s,%s,%s)"""
    dados = (linha[0:10], linha[10:12], linha[12:18])
    return comando, dados

def ins_rl_procedimento_regra_cond(linha):
    comando = """insert into rl_procedimento_regra_cond (
                    CO_PROCEDIMENTO,
                    CO_REGRA_CONDICIONADA)
                values (%s,%s)"""
    dados = (linha[0:10], linha[10:14])
    return comando, dados

def ins_rl_procedimento_servico(linha):
    comando = """insert into rl_procedimento_servico (
                    CO_PROCEDIMENTO,
                    CO_SERVICO,
                    CO_CLASSIFICACAO,
                    DT_COMPETENCIA)
                values (%s,%s,%s,%s)"""
    dados = (linha[0:10], linha[10:13], linha[13:16], linha[16:22])
    return comando, dados

def ins_rl_procedimento_sia_sih(linha):
    comando = """insert into rl_procedimento_sia_sih (
                    CO_PROCEDIMENTO,
                    CO_PROCEDIMENTO_SIA_SIH,
                    TP_PROCEDIMENTO,
                    DT_COMPETENCIA)
                values (%s,%s,%s,%s)"""
    dados = (linha[0:10], linha[10:20].strip(), linha[20:21].strip(), linha[21:27])
    return comando, dados
