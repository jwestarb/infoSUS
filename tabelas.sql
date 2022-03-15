
create table rl_excecao_compatibilidade (
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
    QT_PERMITIDA NUMERIC(4),
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
    VL_PERCENTUAL_SH NUMERIC(7),
    VL_PERCENTUAL_SA NUMERIC(7),
    VL_PERCENTUAL_SP NUMERIC(7),
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
    VL_CAMPOS_IRRADIADOS NUMERIC(4)
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
    QT_MAXIMA_EXECUCAO NUMERIC(4),
    QT_DIAS_PERMANENCIA NUMERIC(4),
    QT_PONTOS NUMERIC(4),
    VL_IDADE_MINIMA NUMERIC(4),
    VL_IDADE_MAXIMA NUMERIC(4),
    VL_SH NUMERIC(10),
    VL_SA NUMERIC(10),
    VL_SP NUMERIC(10),
    CO_FINANCIAMENTO VARCHAR(2),
    CO_RUBRICA VARCHAR(6),
    QT_TEMPO_PERMANENCIA NUMERIC(4),
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
);


ALTER TABLE tb_cid ADD CONSTRAINT pk_cid PRIMARY KEY(co_cid);
ALTER TABLE tb_componente_rede ADD CONSTRAINT pk_componente_rede PRIMARY KEY(co_componente_rede);
ALTER table tb_descricao  ADD CONSTRAINT pk_descricao_procedimento PRIMARY KEY(co_procedimento);
ALTER table tb_descricao_detalhe ADD CONSTRAINT pk_desc_detalhe PRIMARY KEY(co_detalhe);
ALTER table tb_detalhe  ADD CONSTRAINT pk_detalhe PRIMARY KEY(co_detalhe);
ALTER TABLE tb_financiamento ADD CONSTRAINT pk_financiamento PRIMARY KEY(co_financiamento);
ALTER table tb_forma_organizacao  ADD constraint pk_forma_organizacao PRIMARY KEY(co_grupo, co_sub_grupo, co_forma_organizacao);
ALTER table tb_grupo  ADD CONSTRAINT pk_grupo PRIMARY KEY(co_grupo);
ALTER table tb_grupo_habilitacao  ADD CONSTRAINT pk_grupo_habilitacao PRIMARY KEY(nu_grupo_habilitacao);
ALTER table tb_habilitacao  ADD CONSTRAINT PK_HABILITACAO PRIMARY KEY(CO_HABILITACAO);
ALTER table tb_modalidade  ADD CONSTRAINT PK_MODALIDADE PRIMARY KEY(CO_MODALIDADE);
ALTER table tb_ocupacao  ADD CONSTRAINT pk_ocupacao PRIMARY KEY(co_ocupacao);
ALTER TABLE tb_procedimento ADD CONSTRAINT pk_procedimento PRIMARY KEY(co_procedimento);
ALTER table tb_rede_atencao  ADD CONSTRAINT pk_rede_atencao PRIMARY KEY(co_rede_atencao);
ALTER table tb_registro  ADD CONSTRAINT pk_registro PRIMARY KEY(co_registro);
ALTER table tb_regra_condicionada  ADD CONSTRAINT pk_regra_condicionada PRIMARY KEY(co_regra_condicionada);
ALTER table tb_renases  ADD constraint pk_renases PRIMARY KEY(co_renases);
ALTER table tb_rubrica  ADD constraint PK_RUBRICA PRIMARY KEY(CO_RUBRICA);
ALTER table tb_servico  ADD constraint pk_servico PRIMARY KEY(CO_SERVICO);
ALTER table tb_servico_classificacao  ADD constraint pk_servico_classificacao PRIMARY KEY(CO_SERVICO, CO_CLASSIFICACAO);
ALTER table tb_sia_sih  ADD constraint pk_sia_sih PRIMARY KEY(CO_PROCEDIMENTO_SIA_SIH, TP_PROCEDIMENTO);
ALTER table tb_sub_grupo  ADD constraint pk_sub_grupo PRIMARY KEY(CO_GRUPO, CO_SUB_GRUPO);
ALTER table tb_tipo_leito  ADD constraint pk_tipo_leito PRIMARY KEY(co_tipo_leito);
ALTER table tb_tuss  ADD constraint pk_tuss PRIMARY KEY(CO_TUSS);

update tb_procedimento set co_rubrica = NULL where co_rubrica = '';

ALTER TABLE tb_servico_classificacao 
add constraint fk_servico
FOREIGN KEY (co_servico) 
REFERENCES tb_servico (co_servico);

ALTER TABLE rl_procedimento_servico 
add constraint fk_servico_classificacao
FOREIGN KEY (co_servico, co_classificacao) 
REFERENCES tb_servico_classificacao (co_servico, co_classificacao);

ALTER TABLE rl_procedimento_servico 
add constraint fk_procedimento
FOREIGN KEY (co_procedimento) 
REFERENCES tb_procedimento (co_procedimento);

update tb_renases set co_renases = SUBSTRING(co_renases,1,3);

ALTER TABLE rl_procedimento_renases 
add constraint fk_renases
FOREIGN KEY (co_renases) 
REFERENCES tb_renases (co_renases);

ALTER TABLE rl_procedimento_renases 
add constraint fk_procedimento
FOREIGN KEY (co_procedimento) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_procedimento_regra_cond 
add constraint fk_regra_condicionada
FOREIGN KEY (co_regra_condicionada) 
REFERENCES tb_regra_condicionada (co_regra_condicionada);

ALTER TABLE rl_procedimento_regra_cond 
add constraint fk_procedimento
FOREIGN KEY (co_procedimento) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_procedimento_registro 
add constraint fk_registro
FOREIGN KEY (co_registro) 
REFERENCES tb_registro (co_registro);

ALTER TABLE rl_procedimento_registro 
add constraint fk_procedimento
FOREIGN KEY (co_procedimento) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_procedimento_origem 
add constraint fk_procedimento
FOREIGN KEY (co_procedimento) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_procedimento_origem 
add constraint fk_procedimento_origem
FOREIGN KEY (co_procedimento_origem) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_procedimento_ocupacao 
add constraint fk_ocupacao
FOREIGN KEY (co_ocupacao) 
REFERENCES tb_ocupacao (co_ocupacao);

ALTER TABLE rl_procedimento_ocupacao 
add constraint fk_procedimento
FOREIGN KEY (co_procedimento) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_procedimento_modalidade 
add constraint fk_modalidade
FOREIGN KEY (co_modalidade) 
REFERENCES tb_modalidade (co_modalidade);

ALTER TABLE rl_procedimento_modalidade 
add constraint fk_procedimento
FOREIGN KEY (co_procedimento) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_procedimento_leito 
add constraint fk_tipo_leito
FOREIGN KEY (co_tipo_leito) 
REFERENCES tb_tipo_leito (co_tipo_leito);

ALTER TABLE rl_procedimento_leito 
add constraint fk_procedimento
FOREIGN KEY (co_procedimento) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_procedimento_incremento 
add constraint fk_habilitacao
FOREIGN KEY (co_habilitacao) 
REFERENCES tb_habilitacao (co_habilitacao);

ALTER TABLE rl_procedimento_incremento 
add constraint fk_procedimento
FOREIGN KEY (co_procedimento) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_procedimento_habilitacao 
add constraint fk_habilitacao
FOREIGN KEY (co_habilitacao) 
REFERENCES tb_habilitacao (co_habilitacao);

ALTER TABLE rl_procedimento_habilitacao 
add constraint fk_procedimento
FOREIGN KEY (co_procedimento) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_procedimento_detalhe 
add constraint fk_procedimento 
FOREIGN KEY (co_procedimento) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_procedimento_detalhe 
add constraint fk_detalhe 
FOREIGN KEY (co_detalhe) 
REFERENCES tb_detalhe (co_detalhe);

update tb_componente_rede set co_componente_rede = SUBSTRING(co_componente_rede,1,5);

ALTER TABLE rl_procedimento_comp_rede 
add constraint fk_pcr_procedimento 
FOREIGN KEY (co_procedimento) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_procedimento_comp_rede 
add constraint fk_pcr_componente_rede 
FOREIGN KEY (co_componente_rede) 
REFERENCES tb_componente_rede (co_componente_rede);

ALTER TABLE rl_procedimento_compativel 
add constraint fk_pc_procedimento_compativel 
FOREIGN KEY (co_procedimento_compativel) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_procedimento_compativel 
add constraint fk_pc_procedimento_principal 
FOREIGN KEY (co_procedimento_principal) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_procedimento_compativel 
add constraint fk_pc_registro_principal 
FOREIGN KEY (co_registro_principal) 
REFERENCES tb_registro (co_registro);

ALTER TABLE rl_procedimento_compativel 
add constraint fk_pc_registro_compativel 
FOREIGN KEY (co_registro_compativel) 
REFERENCES tb_registro (co_registro);

ALTER TABLE rl_excecao_compatibilidade 
add constraint fk_registro_principal 
FOREIGN KEY (co_registro_principal) 
REFERENCES tb_registro (co_registro);

ALTER TABLE rl_excecao_compatibilidade 
add constraint fk_registro_compativel 
FOREIGN KEY (co_registro_compativel) 
REFERENCES tb_registro (co_registro);

ALTER TABLE rl_excecao_compatibilidade 
add constraint fk_procedimento_compativel 
FOREIGN KEY (co_procedimento_compativel) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_excecao_compatibilidade 
add constraint fk_procedimento_principal 
FOREIGN KEY (co_procedimento_principal) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE rl_excecao_compatibilidade 
add constraint fk_procedimento_restricao 
FOREIGN KEY (co_procedimento_restricao) 
REFERENCES tb_procedimento (co_procedimento);

ALTER TABLE tb_procedimento 
ADD CONSTRAINT fk_financiamento 
FOREIGN KEY (co_financiamento) 
REFERENCES tb_financiamento (co_financiamento);

ALTER TABLE tb_procedimento 
ADD CONSTRAINT fk_rubrica 
FOREIGN KEY (co_rubrica) 
REFERENCES tb_rubrica (co_rubrica);

ALTER TABLE rl_procedimento_cid 
ADD CONSTRAINT fk_procedimento 
FOREIGN KEY (CO_PROCEDIMENTO) 
REFERENCES tb_procedimento (CO_PROCEDIMENTO);

ALTER TABLE rl_procedimento_cid 
ADD CONSTRAINT fk_cid 
FOREIGN KEY (co_cid) 
REFERENCES tb_cid (co_cid);
