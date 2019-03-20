#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Expande DBC para DBF
"""
import os
import sys
import subprocess

def dbc2dbf(arq_dbc, dir_saida):
    if not (os.path.exists(arq_dbc) and os.path.isfile(arq_dbc)):
        return 1
    if not (os.path.exists(dir_saida) and os.path.isdir(dir_saida)):
        return 1

    if sys.platform.startswith('win32'):
        cmd = subprocess.call(["C:\\Tabwin\\dbf2dbc.exe", arq_dbc, dir_saida], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    elif sys.platform.startswith('linux'):
        cmd =subprocess.call(['/usr/local/bin/dbf2dbc.sh', arq_dbc, dir_saida], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        #cmd = subprocess.call(["/usr/local/bin/dbf2dbc.sh", arq_dbc, dir_saida], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

    if (cmd == 0):
        if (os.path.exists(arq_dbc[:-3] + 'dbf')):
            return 0
        else:
            return 1
    else:
        return 1

if __name__ == '__main__':
    teste = dbc2dbf('C:\\Projetos\\infoSUS\\tmp\\RDSC1401.dbc', 'C:\\Projetos\\infoSUS\\tmp\\')
    print(teste)
