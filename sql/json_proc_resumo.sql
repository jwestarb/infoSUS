select array_to_json(array_agg(row_to_json(t)))
from (
select	substr(a.co_procedimento,1,2) co_grupo,
	substr(a.co_procedimento,3,2) co_sub_grupo,
	substr(a.co_procedimento,5,2) co_forma_organizacao,
	a.co_procedimento co_procedimento,
	substr(a.co_procedimento,1,2) || '.' ||
	substr(a.co_procedimento,3,2) || '.' ||
	substr(a.co_procedimento,5,2) || '.' ||
	substr(a.co_procedimento,7,3) || '-' ||
	substr(a.co_procedimento,10,1) co_proc_formatado,
	initcap(a.no_procedimento) no_procedimento
from 	sigtap.tb_procedimento a
) t

