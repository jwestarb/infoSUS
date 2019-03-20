CREATE OR REPLACE FUNCTION sigtap.desc_sexo(text) RETURNS text AS
$BODY$
    SELECT
      CASE 
          WHEN $1 = 'M' THEN 'Masculino'
          WHEN $1 = 'F' THEN 'Feminino'
          WHEN $1 = 'I' THEN 'Indiferente/Ambos'
          WHEN $1 = 'N' THEN 'Não se aplica'
          ELSE 'Não Definida' 
      END
    AS result
$BODY$
LANGUAGE SQL;