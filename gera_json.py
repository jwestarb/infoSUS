#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import csv
import json

current_dir = os.getcwd()
tables_dir = os.path.join(current_dir, 'Sigtap')
layouts_dir = os.path.join(current_dir, 'Sigtap', 'layout')
json_dir = os.path.join(current_dir, 'Sigtap', 'json')


def read_layout_file(file_name):
    with open(file_name, encoding='iso-8859-1') as fl:
        reader = csv.DictReader(fl)
        return list(reader)


if __name__ == "__main__":
    files = [f for f in os.listdir(tables_dir)]

    for file in files:
        if file.endswith('.txt'):
            filename = os.path.join(tables_dir, file)
            filename_noext = file[:-4]
            print('Importando o arquivo: {}'.format(filename))
            try:
                f = open(filename, 'r', encoding='iso-8859-1')
            except IOError as ex:
                print('Não foi possivel abrir o arquivo {}'.format(filename))

            try:
                jsonfile = open(os.path.join(json_dir, '{}.json'.format(
                    filename_noext)), 'w', encoding='utf-8')
            except IOError as ex:
                print('Não foi possivel criar o arquivo {}'.
                      format(filename_noext))

            file_layout = os.path.join(
                layouts_dir, '{}_layout.txt'.format(filename_noext))
            print('Arquivo de Layout: {}'.format(file_layout))

            json_out = {filename_noext: list()}

            for linha in f.readlines():
                reg = dict()

                for row in read_layout_file(file_layout):
                    inicio = int(row['Inicio'])-1
                    fim = int(row['Fim'])
                    reg[row['Coluna']] = linha[inicio:fim].strip()

                json_out[filename_noext].append(reg)

            json.dump(json_out, jsonfile, sort_keys=False,
                      indent=2, separators=(',', ': '), ensure_ascii=False)
            f.close()
            jsonfile.close()
