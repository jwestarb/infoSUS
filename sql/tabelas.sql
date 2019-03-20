
create table sigtap.rl_excecao_compatibilidade (
	CO_PROCEDIMENTO_RESTRICAO VARCHAR(10),
	CO_PROCEDIMENTO_PRINCIPAL VARCHAR(10),
	CO_REGISTRO_PRINCIPAL VARCHAR(2),
	CO_PROCEDIMENTO_COMPATIVEL VARCHAR(10),
	CO_REGISTRO_COMPATIVEL VARCHAR(2),
	TP_COMPATIBILIDADE VARCHAR(1),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.rl_procedimento_cid (
	CO_PROCEDIMENTO VARCHAR(10),
	CO_CID VARCHAR(4),
	ST_PRINCIPAL CHAR(1),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.rl_procedimento_compativel (
	CO_PROCEDIMENTO_PRINCIPAL VARCHAR(10),
	CO_REGISTRO_PRINCIPAL VARCHAR(2),
	CO_PROCEDIMENTO_COMPATIVEL VARCHAR(10),
	CO_REGISTRO_COMPATIVEL VARCHAR(2),
	TP_COMPATIBILIDADE VARCHAR(1),
	QT_PERMITIDA NUMERIC(4),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.rl_procedimento_detalhe (
	CO_PROCEDIMENTO VARCHAR(10),
	CO_DETALHE VARCHAR(3),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.rl_procedimento_habilitacao (
	CO_PROCEDIMENTO VARCHAR(10),
	CO_HABILITACAO VARCHAR(4),
	NU_GRUPO_HABILITACAO VARCHAR(4),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.rl_procedimento_incremento (
	CO_PROCEDIMENTO VARCHAR(10),
	CO_HABILITACAO VARCHAR(4),
	VL_PERCENTUAL_SH NUMERIC(5,2),
	VL_PERCENTUAL_SA NUMERIC(5,2),
	VL_PERCENTUAL_SP NUMERIC(5,2),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.rl_procedimento_leito (
	CO_PROCEDIMENTO VARCHAR(10),
	CO_TIPO_LEITO VARCHAR(2),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.rl_procedimento_modalidade (
	CO_PROCEDIMENTO VARCHAR(10),
	CO_MODALIDADE VARCHAR(2),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.rl_procedimento_ocupacao (
	CO_PROCEDIMENTO VARCHAR(10),
	CO_OCUPACAO CHAR(6),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.rl_procedimento_origem (
	CO_PROCEDIMENTO VARCHAR(10),
	CO_PROCEDIMENTO_ORIGEM VARCHAR(10),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.rl_procedimento_registro (
	CO_PROCEDIMENTO VARCHAR(10),
	CO_REGISTRO VARCHAR(2),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.rl_procedimento_regra_cond (
	CO_PROCEDIMENTO VARCHAR(10),
	CO_REGRA_CONDICIONADA VARCHAR(4)
);

create table sigtap.rl_procedimento_servico (
	CO_PROCEDIMENTO VARCHAR(10),
	CO_SERVICO VARCHAR(3),
	CO_CLASSIFICACAO VARCHAR(3),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.rl_procedimento_sia_sih (
	CO_PROCEDIMENTO VARCHAR(10),
	CO_PROCEDIMENTO_SIA_SIH VARCHAR(10),
	TP_PROCEDIMENTO VARCHAR(1),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.tb_cid (
	CO_CID VARCHAR(4),
	NO_CID VARCHAR(100),
	TP_AGRAVO CHAR(1),
	TP_SEXO CHAR(1),
	TP_ESTADIO CHAR(1),
	VL_CAMPOS_IRRADIADOS NUMERIC(4)
);

create table sigtap.tb_descricao_detalhe (
	CO_DETALHE VARCHAR(3),
	DS_DETALHE VARCHAR(4000),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.tb_descricao (
	CO_PROCEDIMENTO VARCHAR(10),
	DS_PROCEDIMENTO VARCHAR(4000),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.tb_detalhe (
	CO_DETALHE VARCHAR(3),
	NO_DETALHE VARCHAR(100),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.tb_financiamento (
	CO_FINANCIAMENTO VARCHAR(2),
	NO_FINANCIAMENTO VARCHAR(100),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.tb_forma_organizacao (
	CO_GRUPO VARCHAR(2),
	CO_SUB_GRUPO VARCHAR(2),
	CO_FORMA_ORGANIZACAO VARCHAR(2),
	NO_FORMA_ORGANIZACAO VARCHAR(100),
	DT_COMPETENCIA CHAR(6)
);
ALTER TABLE sigtap.tb_forma_organizacao ADD CONSTRAINT tb_forma_organizacao_pk PRIMARY KEY (CO_GRUPO, CO_SUB_GRUPO, CO_FORMA_ORGANIZACAO);
COMMENT ON TABLE sigtap.tb_forma_organizacao IS 'Forma de Organização dos Procedimentos';
COMMENT ON COLUMN sigtap.tb_forma_organizacao.co_grupo IS 'Código do grupo dos procedimentos';
COMMENT ON COLUMN sigtap.tb_forma_organizacao.co_sub_grupo IS 'Código do sub-grupo dos procedimentos';
COMMENT ON COLUMN sigtap.tb_forma_organizacao.co_forma_organizacao IS 'Código da forma de organização dos procedimentos';
COMMENT ON COLUMN sigtap.tb_forma_organizacao.no_forma_organizacao IS 'Nome da forma de organização dos procedimento';
COMMENT ON COLUMN sigtap.tb_forma_organizacao.dt_competencia IS 'Data que informa a competência de validade deste registro';

create table sigtap.tb_grupo_habilitacao (
	NU_GRUPO_HABILITACAO VARCHAR(4),
	NO_GRUPO_HABILITACAO VARCHAR(20),
	DS_GRUPO_HABILITACAO VARCHAR(250)
);

create table sigtap.tb_grupo (
	CO_GRUPO VARCHAR(2),
	NO_GRUPO VARCHAR(100),
	DT_COMPETENCIA CHAR(6)
);
ALTER TABLE sigtap.tb_grupo ADD CONSTRAINT tb_grupo_pk PRIMARY KEY (CO_GRUPO);

COMMENT ON TABLE sigtap.tb_grupo IS 'Grupos de Procedimentos';
COMMENT ON COLUMN sigtap.tb_grupo.co_grupo IS 'Código do grupo dos procedimentos';
COMMENT ON COLUMN sigtap.tb_grupo.no_grupo IS 'Nome do grupo dos procedimentos';
COMMENT ON COLUMN sigtap.tb_grupo.dt_competencia IS 'Data que informa a competência de validade deste registro';


create table sigtap.tb_habilitacao (
	CO_HABILITACAO VARCHAR(4),
	NO_HABILITACAO VARCHAR(150),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.tb_modalidade (
	CO_MODALIDADE VARCHAR(2),
	NO_MODALIDADE VARCHAR(100),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.tb_ocupacao (
	CO_OCUPACAO CHAR(6),
	NO_OCUPACAO VARCHAR(150)
);

create table sigtap.tb_procedimento (
	CO_PROCEDIMENTO VARCHAR(10),
	NO_PROCEDIMENTO VARCHAR(250),
	TP_COMPLEXIDADE VARCHAR(1),
	TP_SEXO VARCHAR(1),
	QT_MAXIMA_EXECUCAO NUMERIC(4),
	QT_DIAS_PERMANENCIA NUMERIC(4),
	QT_PONTOS NUMERIC(4),
	VL_IDADE_MINIMA NUMERIC(4),
	VL_IDADE_MAXIMA NUMERIC(4),
	VL_SH NUMERIC(8,2),
	VL_SA NUMERIC(8,2),
	VL_SP NUMERIC(8,2),
	CO_FINANCIAMENTO VARCHAR(2),
	CO_RUBRICA VARCHAR(6),
	QT_TEMPO_PERMANENCIA NUMERIC(4),
	DT_COMPETENCIA CHAR(6)
);
ALTER TABLE sigtap.tb_procedimento ADD CONSTRAINT tb_procedimento_pk PRIMARY KEY (CO_PROCEDIMENTO);
COMMENT ON TABLE sigtap.tb_procedimento IS 'Procedimentos';
COMMENT ON COLUMN sigtap.tb_procedimento.co_procedimento IS 'Código do procedimento';


create table sigtap.tb_registro (
	CO_REGISTRO VARCHAR(2),
	NO_REGISTRO VARCHAR(50),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.tb_regra_condicionada (
	CO_REGRA_CONDICIONADA VARCHAR(4),
	NO_REGRA_CONDICIONADA VARCHAR(150),
	DS_REGRA_CONDICIONADA VARCHAR(4000)
);

create table sigtap.tb_rubrica (
	CO_RUBRICA VARCHAR(6),
	NO_RUBRICA VARCHAR(100),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.tb_servico_classificacao (
	CO_SERVICO VARCHAR(3),
	CO_CLASSIFICACAO VARCHAR(3),
	NO_CLASSIFICACAO VARCHAR(150),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.tb_servico (
	CO_SERVICO VARCHAR(3),
	NO_SERVICO VARCHAR(120),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.tb_sia_sih (
	CO_PROCEDIMENTO_SIA_SIH VARCHAR(10),
	NO_PROCEDIMENTO_SIA_SIH VARCHAR(100),
	TP_PROCEDIMENTO VARCHAR(1),
	DT_COMPETENCIA CHAR(6)
);

create table sigtap.tb_sub_grupo (
	CO_GRUPO VARCHAR(2),
	CO_SUB_GRUPO VARCHAR(2),
	NO_SUB_GRUPO VARCHAR(100),
	DT_COMPETENCIA CHAR(6)
);
ALTER TABLE sigtap.tb_sub_grupo ADD CONSTRAINT tb_sub_grupo_pk PRIMARY KEY (CO_GRUPO, CO_SUB_GRUPO);
COMMENT ON TABLE sigtap.tb_sub_grupo IS 'Sub-Grupos de Procedimentos';
COMMENT ON COLUMN sigtap.tb_sub_grupo.co_grupo IS 'Código do grupo dos procedimentos';
COMMENT ON COLUMN sigtap.tb_sub_grupo.co_sub_grupo IS 'Código do sub-grupo dos procedimentos';
COMMENT ON COLUMN sigtap.tb_sub_grupo.no_sub_grupo IS 'Nome do sub-grupo dos procedimento';
COMMENT ON COLUMN sigtap.tb_sub_grupo.dt_competencia IS 'Data que informa a competência de validade deste registro';

create table sigtap.tb_tipo_leito (
	CO_TIPO_LEITO VARCHAR(2),
	NO_TIPO_LEITO VARCHAR(60),
	DT_COMPETENCIA CHAR(6)
);
