select	a.co_procedimento co_procedimento,
	substr(a.co_procedimento,1,2) || '.' ||
	substr(a.co_procedimento,3,2) || '.' ||
	substr(a.co_procedimento,5,2) || '.' ||
	substr(a.co_procedimento,7,3) || '-' ||
	substr(a.co_procedimento,9,1) co_proc_formatado,
	initcap(a.no_procedimento) no_procedimento,
	sigtap.desc_complexidade(a.tp_complexidade) ds_complexidade,
	sigtap.desc_sexo(a.tp_sexo) ds_sexo,
	a.qt_maxima_execucao,
	a.qt_dias_permanencia,
	a.qt_pontos,
	round(a.vl_idade_minima/12) || ' Anos' vl_idade_minima,
	round(a.vl_idade_maxima/12) || ' Anos' vl_idade_maxima,
	a.vl_sh,
	a.vl_sa,
	a.vl_sp,
	sigtap.desc_financiamento(a.co_financiamento) ds_financiamento,
	a.co_rubrica,
	a.qt_tempo_permanencia
from 	sigtap.tb_procedimento a
limit 10

