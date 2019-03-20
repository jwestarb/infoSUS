CREATE OR REPLACE FUNCTION sigtap.desc_tipo_leito(text) RETURNS text AS
$BODY$
    SELECT
      CASE 
	        WHEN $1 = '01' THEN 'Cirúrgico'
			WHEN $1 = '02' THEN 'Obstétricos'
			WHEN $1 = '03' THEN 'Clínico'
			WHEN $1 = '04' THEN 'Crônicos'
			WHEN $1 = '05' THEN 'Psiquiatria'
			WHEN $1 = '06' THEN 'Pneumologia Sanitária (Tisiologia)'
			WHEN $1 = '07' THEN 'Pediátricos'
			WHEN $1 = '08' THEN 'Reabilitação'
			WHEN $1 = '09' THEN 'Leito Dia / Cirúrgicos'
			WHEN $1 = '10' THEN 'Leito Dia / Aids'
			WHEN $1 = '11' THEN 'Leito Dia / Fibrose Cística'
			WHEN $1 = '12' THEN 'Leito Dia / Intercorrência Pós-Transplante'
			WHEN $1 = '13' THEN 'Leito Dia / Geriatria'
			WHEN $1 = '14' THEN 'Leito Dia / Saúde Mental'
			WHEN $1 = '64' THEN 'Unidade Intermediária'
			WHEN $1 = '65' THEN 'Unidade Intermediária Neonatal'
			WHEN $1 = '74' THEN 'UTI I'
			WHEN $1 = '75' THEN 'UTI Adulto II'
			WHEN $1 = '76' THEN 'UTI Adulto III'
			WHEN $1 = '77' THEN 'UTI Infantil I'
			WHEN $1 = '78' THEN 'UTI Infantil II'
			WHEN $1 = '79' THEN 'UTI Infantil III'
			WHEN $1 = '80' THEN 'UTI Neonatal I'
			WHEN $1 = '81' THEN 'UTI Neonatal II'
			WHEN $1 = '82' THEN 'UTI Neonatal III'
			WHEN $1 = '83' THEN 'UTI Queimados'
            ELSE 'Não Definido' 
      END
    AS result
$BODY$
LANGUAGE SQL;



