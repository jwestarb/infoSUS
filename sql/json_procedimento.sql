select array_to_json(array_agg(row_to_json(t)))
from (
    select *
    from sigtap.tb_procedimento a
) t

