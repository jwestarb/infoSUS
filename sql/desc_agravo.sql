CREATE OR REPLACE FUNCTION sigtap.desc_agravo(text) RETURNS text AS
$BODY$
    SELECT
      CASE 
	        WHEN $1 = '1' THEN 'Sem Agravo'
			WHEN $1 = '2' THEN 'Agravo de notificação'
			WHEN $1 = '3' THEN 'Agravo de bloqueio'
            ELSE 'Não Definido' 
      END
    AS result
$BODY$
LANGUAGE SQL;
