CREATE OR REPLACE FUNCTION sigtap.desc_compatibilidade(text) RETURNS text AS
$BODY$
    SELECT
      CASE 
	        WHEN $1 = '1' THEN 'Compatível'
			WHEN $1 = '2' THEN 'Incompatível / Excludente'
			WHEN $1 = '3' THEN 'Concomitante'
            ELSE 'Não Definida' 
      END
    AS result
$BODY$
LANGUAGE SQL;