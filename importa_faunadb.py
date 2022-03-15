import sys
import os
import csv
import json
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

current_dir = os.getcwd()
tables_dir = os.path.join(current_dir, 'Sigtap')
layouts_dir = os.path.join(current_dir, 'Sigtap', 'layout')


def read_layout_file(file_name):
    with open(file_name, encoding='iso-8859-1') as fl:
        reader = csv.DictReader(fl)
        return list(reader)


if __name__ == "__main__":
    client = FaunaClient(secret='fnAEExm8DfACCRQ3ZqKHFlMjM-0cU59pNo7UDkAW')
    
    # files = [f for f in os.listdir(tables_dir)]
    files = ['tb_grupo.txt']

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
            print('Arquivo de Layout: {}'.format(file_layout))

            json_out = list()

            #coll = client.query(q.create_collection({"name": filename_noext}))

            for linha in f.readlines():
                reg = dict()

                for row in read_layout_file(file_layout):
                    inicio = int(row['Inicio']) - 1
                    fim = int(row['Fim'])
                    reg[row['Coluna'].lower()] = linha[inicio:fim].strip()

                json_out.append(reg)
            if (len(json_out) > 0):
                
                for reg in json_out:
                    print(reg)
                    doc  = client.query(q.create(filename_noext, {"data": reg}))
            
            f.close()  

