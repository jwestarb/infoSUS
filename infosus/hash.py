#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Gera Hash MD5 de um arquivo
"""
import os
import hashlib

def md5_arquivo(caminhoArquivo, block_size = 1048576, retornoHex = True):
    """
    Tamanho do bloco depende diretamente do tamanho do bloco de seu sistema de arquivos
    para evitar problemas de performance.
    Aqui eu tenho blocos de 4096 octetos (padrão NTFS)
    """
    if os.path.exists(caminhoArquivo) == False:
        return None
    f = open(caminhoArquivo, 'rb')
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    f.close()
    if retornoHex:
        return md5.hexdigest()
    return md5.digest()

if __name__ == '__main__':
    teste = md5_arquivo('PASC1312.dbc')
    print(teste)
