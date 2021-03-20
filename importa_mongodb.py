#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import csv
import json
import pymongo

current_dir = os.getcwd()
tables_dir = os.path.join(current_dir, 'Sigtap')
layouts_dir = os.path.join(current_dir, 'Sigtap', 'layout')


def read_layout_file(file_name):
    with open(file_name, encoding='iso-8859-1') as fl:
        reader = csv.DictReader(fl)
        return list(reader)


if __name__ == "__main__":
    # client = pymongo.MongoClient('mongodb://localhost:27017/')
    client = pymongo.MongoClient('mongodb+srv://jwestarb:xof6dM1akIk0bOnO@cluster0-4rg30.gcp.mongodb.net/week10?authSource=admin&replicaSet=Cluster0-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true')
    db = client.sigtap
    
    files = [f for f in os.listdir(tables_dir)]

    for file in files:
        if file.endswith('.txt'):
            filename = os.path.join(tables_dir, file)
            filename_noext = file[:-4]
            # print('Importando o arquivo: {}'.format(filename))
            try:
                f = open(filename, 'r', encoding='iso-8859-1')
            except IOError as ex:
                print(ex)
                print('Não foi possivel abrir o arquivo {}'.format(filename))
                sys.exit(-1)

            file_layout = os.path.join(
                layouts_dir, '{}_layout.txt'.format(filename_noext))
            # print('Arquivo de Layout: {}'.format(file_layout))

            json_out = list()
            collection = db[filename_noext]            

            for linha in f.readlines():
                reg = dict()

                for row in read_layout_file(file_layout):
                    inicio = int(row['Inicio']) - 1
                    fim = int(row['Fim'])
                    reg[row['Coluna'].lower()] = linha[inicio:fim].strip()

                json_out.append(reg)
            if (len(json_out) > 0):
                result = collection.insert_many(json_out)
                print('{} - inseridos: {} registros.'.format(filename_noext, len(result.inserted_ids)))
            
            f.close()  
    
    client.close()          
