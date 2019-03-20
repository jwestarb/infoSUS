#!/bin/sh

declare -a estados=("AC" "AL" "AM" "AP" "BA" "CE" "DF" "ES" "GO" "MA" "MG" "MS" "MT" "PA" "PB" "PE" "PI" "PR" "RJ" "RN" "RO" "RR" "RS" "SC" "SE" "SP" "TO")
dir="/dados"

for i in "${estados[@]}"
do
   mkdir "dados_$i"
   mkdir "dados_$i/CIHA"
   mkdir "dados_$i/SIA"
   mkdir "dados_$i/SIH"
   chown -R postgres.postgres "dados_$i"
   chmod 700 "dados_$i"
   #psql -U postgres -c "CREATE TABLESPACE dados_"$i"_CIHA OWNER postgres LOCATION '$dir/dados_$i/CIHA';"
   #psql -U postgres -c "CREATE TABLESPACE dados_"$i"_SIA OWNER postgres LOCATION '$dir/dados_$i/SIA';"
   #psql -U postgres -c "CREATE TABLESPACE dados_"$i"_SIH OWNER postgres LOCATION '$dir/dados_$i/SIH';"
done
