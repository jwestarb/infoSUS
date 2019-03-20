#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Python source code - replace this with a description of the code and write the code below this text.
"""
import traceback
import urllib2
import httplib
import socket
from bs4 import BeautifulSoup

def busca_estab_mun(estado, municipio):
    estabs = []

    req = urllib2.Request('http://cnes.datasus.gov.br/Lista_Es_Municipio.asp?VEstado=' + estado + '&VCodMunicipio=' + municipio)
    req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')

    try:
        html = urllib2.urlopen(req, timeout=30)
        soup = BeautifulSoup(html)
        table = soup.find_all('table')[4]

        for linha in table.findAll("tr"):
            estab = {}
            cells = linha.findAll("td")
            estab['nome'] = cells[0].text
            estab['cnes'] = cells[1].text
            estab['cnpj'] = cells[2].text
            estab['gestao'] = cells[3].text
            estabs.append(estab)
        return estabs

    except urllib2.HTTPError as e:
        print 'HTTPError: ', str(e.code)
    except urllib2.URLError as e:
        print 'URLError: ', str(e.reason)
    except httplib.HTTPException, e:
        print 'HTTPException: ', + traceback.format_exc()
    except socket.timeout:
        print 'Timeout: ' + traceback.format_exc()
    except IndexError:
        print 'ERRO LENDO TABELAS DO HTML municipio: ', municipio
        print html.read()
    except Exception:
        print 'Erro generico: ' + traceback.format_exc()

    return estabs
