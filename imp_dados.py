#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
InfoSUS
"""
import argparse
from infosus import sih
from infosus import sia
from infosus import ciha

parser = argparse.ArgumentParser(description='Importa arquivos de dados do DataSUS.')
parser.add_argument("tipo", help="Tipo de arquivo: SIH, SIA ou CIHA")
parser.add_argument("ano", help="Ano a ser importado")
parser.add_argument("--estado", help="Estado a ser importado")
parser.add_argument("--mes", help="Mês a ser importado", choices=['01','02','03','04','05','06','07','08','09','10','11','12'])
args = parser.parse_args()

if args.tipo == 'SIH':
    sih.importa_sih(args.estado, args.ano, args.mes)
elif args.tipo == 'SIA':
    sia.importa_sia_sqlite(args.estado, args.ano, args.mes)
elif args.tipo == 'RSIA':
    sia.gera_resumo(args.estado, args.ano, args.mes)
elif args.tipo == 'CIHA':
    ciha.importa_ciha(args.estado, args.ano, args.mes)
else:
    parser.print_help()
