select count(*) from dados.dados_sih where ano_cmpt = '2014'

select count(*) from dados.dados_sia

select id_arqdados, count(*)
from dados.dados_sih
group by id_arqdados

select id_arqdados, count(*)
from dados.dados_sia
group by id_arqdados

select id_arqdados, count(*)
from dados.dados_ciha
group by id_arqdados

select * from arquivo_dados where tipo = 'SIH' and sub_tipo = 'RD' and estado = 'SC' order by ano, mes

select * from arquivo_dados where tipo = 'SIA' and sub_tipo = 'PA' and estado = 'SC' order by ano, mes

select * from arquivo_dados where tipo = 'CIHA' and sub_tipo = 'CIHA' and estado = 'SC' and ano = '2014' order by ano, mes


select  pa_mvm,
        pa_cnpjmnt,
        pa_cnpjcpf,
        pa_coduni,
        sum(pa_qtdapr) pa_qtdapr,
        sum(pa_valapr) pa_valapr,
        sum(pa_qtdpro) pa_qtdpro,
        sum(pa_valpro) pa_valpro,
        sum(pa_vl_cf) pa_vl_cf,
        sum(pa_vl_cl) pa_vl_cl,
        sum(pa_vl_inc) pa_vl_inc,
        sum(pa_dif_val) pa_dif_val
from 	  dados.sia
where   pa_cnpjmnt = '83883306000160'
group by pa_mvm, pa_cnpjmnt, pa_cnpjcpf, pa_coduni,


CREATE TABLE dados.sia_resumo
(
  id serial NOT NULL,
  id_arqdados bigint NOT NULL,
  dt_cmpt date  NOT NULL,
  pa_mvm character varying(6),
  pa_ufmun character varying(6),
  pa_cnpjmnt character varying(14),
  pa_cnpjcpf character varying(14),
  pa_coduni character varying(7),
  pa_tpups character varying(2),
  pa_tippre character varying(2),
  pa_docorig character varying(1),
  pa_qtdapr numeric(15,0),
  pa_valapr numeric(20,2),
  pa_qtdpro numeric(15,0),
  pa_valpro numeric(20,2),
  pa_vl_cf numeric(20,2),
  pa_vl_cl numeric(20,2),
  pa_vl_inc numeric(20,2),
  pa_dif_val numeric(20,2),
  CONSTRAINT sia_resumo_pkey PRIMARY KEY (id)
) TABLESPACE dados_sia;

select  pa_mvm,
        pa_ufmun,
        pa_cnpjmnt,
        pa_cnpjcpf,
        pa_coduni,
        pa_tpups,
        pa_tippre,
        pa_docorig,
        sum(pa_qtdapr) pa_qtdapr,
        sum(pa_valapr) pa_valapr,
        sum(pa_qtdpro) pa_qtdpro,
        sum(pa_valpro) pa_valpro,
        sum(pa_vl_cf) pa_vl_cf,
        sum(pa_vl_cl) pa_vl_cl,
        sum(pa_vl_inc) pa_vl_inc,
        sum(pa_dif_val) pa_dif_val
from    sia
group by pa_mvm, pa_ufmun, pa_cnpjmnt, pa_cnpjcpf, pa_coduni, pa_tpups, pa_tippre, pa_docorig
order by 1,2,3,4,5,6,7,8
