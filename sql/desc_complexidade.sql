CREATE OR REPLACE FUNCTION sigtap.desc_complexidade(text) RETURNS text AS
$BODY$
    SELECT
      CASE 
          WHEN $1 = '0' THEN 'Não se aplica'
          WHEN $1 = '1' THEN 'Atenção Básica Complexidade'
          WHEN $1 = '2' THEN 'Média Complexidade'
          WHEN $1 = '3' THEN 'Alta Complexidade'
          ELSE 'Não Definida' 
      END
    AS result
$BODY$
LANGUAGE SQL;