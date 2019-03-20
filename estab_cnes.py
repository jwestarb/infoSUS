#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Importa dados de um estabelecimento do site http://cnes.datasus.gov.br
"""
import traceback
import urllib.request, urllib.parse, urllib.error
import http.client
import socket
from bs4 import BeautifulSoup

def busca_estab(codcnes, codibge):
    estab = {}
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'
    vco_Unidade = codibge + codcnes.zfill(7)

    req = urllib.request.Request('http://cnes.datasus.gov.br/Exibe_Ficha_Estabelecimento.asp?VCo_Unidade=' + vco_Unidade)
    req.add_header('User-agent', user_agent)
    req2 = urllib.request.Request('http://cnes.datasus.gov.br/Mod_Basico.asp?VCo_Unidade=' + vco_Unidade)
    req2.add_header('User-agent', user_agent)

    try:
        html = urllib.request.urlopen(req, timeout=30)
        soup = BeautifulSoup(html, "lxml")
        table = soup.findAll('table')[4]

        html2 = urllib.request.urlopen(req2, timeout=30)
        soup2 = BeautifulSoup(html2, "lxml")
        table2 = soup2.findAll('table')[5]

        linhas_ficha  = table.findAll("td")
        linhas_basico = table2.findAll("td")

        estab['razaoSocial'] = linhas_basico[14].text
        estab['cnpj'] = linhas_basico[49].text
        estab['cpf'] = linhas_basico[50].text
        estab['personalidade'] = linhas_basico[6].text.strip()
        estab['logradouro'] = linhas_basico[15].text
        estab['numero'] = linhas_basico[23].text
        estab['complemento'] = linhas_basico[24].text
        estab['bairro'] = linhas_basico[25].text
        estab['cep'] = linhas_basico[26].text
        estab['telefone'] = linhas_basico[47].text
        estab['cnpjMantenedora'] = linhas_basico[51].text
        estab['email'] = linhas_basico[48].text
        estab['fax'] = linhas_basico[39].text
        estab['dependencia'] = linhas_basico[9].text.strip()
        estab['terceiros'] = linhas_basico[10].text.strip()
        estab['regiaoSaude'] = linhas_basico[35].text

        estab['nome'] = linhas_ficha[3].text
        estab['tipoEstab'] = linhas_ficha[32].text
        estab['subTipoEstab'] = linhas_ficha[33].text
        estab['esferaAdm'] = linhas_ficha[34].text.strip()
        estab['gestaoExtenso'] = linhas_ficha[35].text
        estab['naturezaOrg'] = linhas_ficha[38].text

        #for idx, linha in enumerate(table2.findAll("td")):
            #print str(idx) + ' = ' + linha.text

    except urllib.error.HTTPError as e:
        print('HTTPError: ', str(e.code))
    except urllib.error.URLError as e:
        print('URLError: ', str(e.reason))
    except http.client.HTTPException as e:
        print('HTTPException: ', + traceback.format_exc())
    except socket.timeout:
        print('Timeout: ' + traceback.format_exc())
    except IndexError:
        print('ERRO LENDO TABELAS DO HTML: ', codcnes.zfill(7))
        print(html.read())

    return estab

if __name__ == '__main__':
    teste = busca_estab('2558246', '420240')
    print(teste)
