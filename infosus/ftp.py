#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Funções para conexão FTP
"""
import os
import ftplib
import ftputil
import ftputil.session

class FtpError(Exception):
    pass

class FtpClient(object):

    def __init__(self, host, user, password, port = 21):
        try:
            self.jc_session_factory = ftputil.session.session_factory(
                                   base_class=ftplib.FTP,
                                   port=port,
                                   use_passive_mode=True,
                                   encrypt_data_channel=False)
            self.ftp = ftputil.FTPHost(host, user, password, session_factory = self.jc_session_factory)
            self.ftp.use_list_a_option = False
            self.total_size = 0
            self.received = 0
        except ftputil.error.FTPOSError:
            raise FtpError

    def download_callback(self, chunk):
        self.received += len(chunk)
        print("Download: {} bytes / {} bytes".format(self.received, self.total_size), end='\r')

    def altera_diretorio(self, diretorio):
        self.ftp.chdir(diretorio)

    def download_log(self, remoto, local):
        self.total_size = self.ftp.stat(remoto).st_size
        data_hora_alt = self.ftp.path.getmtime(remoto)
        self.ftp.download_if_newer(remoto, local, callback=self.download_callback)
        os.utime(local, (data_hora_alt,data_hora_alt))

    def download(self, remoto, local):
        data_hora_alt = self.ftp.path.getmtime(remoto)
        self.ftp.download_if_newer(remoto, local)
        os.utime(local, (data_hora_alt,data_hora_alt))

    def lista_arquivos(self, diretorio):
        return self.ftp.listdir(diretorio)

if __name__ == '__main__':
    ftp = FtpClient('ftp.datasus.gov.br', 'anonymous', 'tabwin@tabwin.com.br')
    ftp.download('/dissemin/publicos/SIHSUS/200801_/Dados/RDSC1411.dbc','RDSC1411.dbc')
    #arquivos = ftp.lista_arquivos('/dissemin/publicos/SIHSUS/200801_/Dados')
    #for name in arquivos:
        #print(name)
        #if host.path.isfile(name):
            # Remote name, local name, binary mode
            #host.download(name, name)
