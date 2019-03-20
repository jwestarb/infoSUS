CREATE OR REPLACE FUNCTION sigtap.desc_financiamento(text) RETURNS text AS
$BODY$
    SELECT
      CASE 
	        WHEN $1 = '01' THEN 'Atenção Básica (PAB)'
			WHEN $1 = '02' THEN 'Assistência Farmacêutica'
			WHEN $1 = '04' THEN 'Fundo de Ações Estratégicas e Compensações (FAEC)'
			WHEN $1 = '05' THEN 'Incentivo - MAC'
			WHEN $1 = '06' THEN 'Média e Alta Complexidade (MAC)'
			WHEN $1 = '07' THEN 'Vigilância em Saúde'
			WHEN $1 = '08' THEN 'Gestão do SUS'
            ELSE 'Não Definida' 
      END
    AS result
$BODY$
LANGUAGE SQL;
