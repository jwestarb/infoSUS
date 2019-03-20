select array_to_json(array_agg(row_to_json(t))) 
from (
    select co_grupo, no_grupo,
    ( 
      select  array_to_json ( array_agg ( row_to_json ( d ))) 
      from  ( 
        select co_sub_grupo, no_sub_grupo,
        (
        select  array_to_json ( array_agg ( row_to_json ( f ))) 
	from  ( 
         select co_forma_organizacao, no_forma_organizacao
         from sigtap.tb_forma_organizacao c
         where c.co_sub_grupo = b.co_sub_grupo
         and c.co_grupo = b.co_grupo ) f
        ) as formas_organizacao
        from  sigtap.tb_sub_grupo b
        where  a.co_grupo = b.co_grupo
      )  d 
    )  as  sub_grupos
    from sigtap.tb_grupo a
) t

