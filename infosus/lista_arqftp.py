#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Lista Arquivos do FTP
"""
import time
from datetime import datetime
from ftp import FtpClient
import psycopg2

def lista_arquivos(tipo):
    if tipo == 'SIH':
        diretorio = '/dissemin/publicos/SIHSUS/200801_/Dados/'
    elif tipo == 'SIA':
        diretorio = '/dissemin/publicos/SIASUS/200801_/Dados/'
    elif tipo == 'CIHA':
        diretorio = '/dissemin/publicos/CIHA/201101_/Dados/'
    else:
        raise ValueError('Tipo inválido. Use: SIA, SIH ou CIHA')

    ftp = FtpClient('ftp.datasus.gov.br', 'anonymous', 'tabwin@tabwin.com.br')
    ftp.altera_diretorio(diretorio)
    arquivos = ftp.lista_arquivos(diretorio)

    lista = []
    for nome in arquivos:
        arq = {}
        if (ftp.ftp.path.isfile(nome) and (nome[-3:] == 'dbc' or nome[-3:] == 'DBC')):
            arq['nome'] = nome
            arq['tipo'] = tipo
            arq['dir_remoto'] = diretorio
            arq['tamanho'] = ftp.ftp.stat(nome).st_size
            arq['data_hora'] = ftp.ftp.path.getmtime(nome)
            if tipo == 'CIHA':
                arq['mes'] = nome[8:10]
                arq['ano'] = '20' + nome[6:8]
                arq['estado'] = nome[4:6]
                arq['sub_tipo'] = nome[0:4]
            else:
                arq['mes'] = nome[6:8]
                arq['ano'] = '20' + nome[4:6]
                arq['estado'] = nome[2:4]
                arq['sub_tipo'] = nome[0:2]
            lista.append(arq)

    return lista


if __name__ == '__main__':
    ini = time.time()
    try:
        conn = psycopg2.connect("host=192.168.0.88 dbname=siteatw user=postgres password=secret")
    except psycopg2.Error as e:
        print("Erro na conexão com o Banco de Dados: " + e.pgerror)

    cur = conn.cursor()
    sql = """INSERT INTO arquivo_dados2(ano, caminho, data_hora_alt, estado, mes, nome, sub_tipo, tamanho, tipo, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    arq_dados = lista_arquivos('CIHA')
    for arquivo in arq_dados:
        cur.execute(sql, (
            arquivo['ano'],
            arquivo['dir_remoto'],
            datetime.fromtimestamp(arquivo['data_hora']),
            arquivo['estado'],
            arquivo['mes'],
            arquivo['nome'],
            arquivo['sub_tipo'],
            arquivo['tamanho'],
            arquivo['tipo'],
            'NOVO'
        ))
        #print(time.localtime(arquivo['data_hora']))

    conn.commit()
    conn.close()
    fim = time.time()
    print("Tempo lista_arquivos: {} seg".format(fim - ini))
