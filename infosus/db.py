#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Conexão com o Postgresql
"""
import psycopg2
from psycopg2.extras import DictCursor

def get_conn():
    try:
        conn = psycopg2.connect("host=192.168.0.88 dbname=siteatw user=postgres password=secret", cursor_factory=DictCursor)
        #cur.execute("set search_path to dados")
        return conn
    except psycopg2.Error as e:
        print("Erro na conexão com o Banco de Dados: " + e.pgerror)
