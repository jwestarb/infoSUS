import os
import re
import datetime
from ftplib import FTP, error_perm
from dateutil import parser
from io import IOBase, BytesIO
import progressbar

class jcFtp(object):
    """ A wrapper for FTP connections """
    conn = None
    tmp_output = None
    relative_paths = set(['.', '..'])
    pbar = None
    local_file = None
    total_data = 0

    def __init__(self, host, user, password,
            passive=True, ftp_conn=None, **kwargs):

        if ftp_conn:
            self.conn = ftp_conn
        else:
            self.conn = FTP(host=host, user=user, passwd=password, **kwargs)

        if not passive:
            self.conn.set_pasv(False)

    def __getattr__(self, name):
        """ Pass anything we don't know about, to underlying ftp connection """
        def wrapper(*args, **kwargs):
            method = getattr(self.conn, name)
            return method(*args, **kwargs)
        return wrapper

    def cd(self, remote):
        """ Change working directory on server """
        try:
            self.conn.cwd(remote)
        except Exception:
            return False
        else:
            return self.pwd()

    def pwd(self):
        """ Return the current working directory """
        return self.conn.pwd()

    def close(self):
        """ End the session """
        try:
            self.conn.quit()
        except Exception:
            self.conn.close()

    def _collector(self, line):
        """ Helper for collecting output from dir() """
        self.tmp_output.append(line)

    def size(self, filename):
        """ Return size of de filename """
        return self.conn.size(filename)

    def startProgressBar(self, maxval):
        self.pbar = progressbar.ProgressBar(maxval = maxval)
        self.pbar.start()

    def file_write(self, data):
        self.local_file.write(data)
        self.total_data += len(data)
        self.pbar.update(self.total_data)

    def get(self, remote, local=None):
        """ Gets the file from FTP server
            local can be:
                a file: opened for writing, left open
                a string: path to output file
                None: contents are returned
        """
        if isinstance(local, IOBase):  # open file, leave open
            self.local_file = local
        elif local is None:  # return string
            self.local_file = BytesIO()
        else:  # path to file, open, write/close return None
            self.local_file = open(local, 'wb')
        
        file_size = self.size(remote)
        self.startProgressBar(file_size)

        try:
            self.conn.retrbinary("RETR %s" % remote, self.file_write)
        except:
            print("Error transfer file")
        
        self.pbar.finish()

        if isinstance(local, IOBase):
            pass
        elif local is None:
            contents = self.local_file.getvalue()
            self.local_file.close()
            return contents
        else:
            self.local_file.close()

        return None

    def list(self, remote='.', extra=False, remove_relative_paths=False):
        """ Return directory list """
        if extra:
            self.tmp_output = []
            self.conn.dir(remote, self._collector)
            directory_list = split_file_info(self.tmp_output)
        else:
            directory_list = self.conn.nlst(remote)

        if remove_relative_paths:
            return list(filter(self.is_not_relative_path, directory_list))

        return directory_list


def split_file_info(fileinfo):
    """ Parse sane directory output usually ls -l
        Adapted from https://gist.github.com/tobiasoberrauch/2942716
    """
    current_year = datetime.datetime.now().strftime('%Y')
    files = []
    for line in fileinfo:
        parts = re.split(
            r'^([\-dbclps])' +                  # Directory flag [1]
            r'([\-rwxs]{9})\s+' +               # Permissions [2]
            r'(\d+)\s+' +                       # Number of items [3]
            r'([a-zA-Z0-9_-]+)\s+' +            # File owner [4]
            r'([a-zA-Z0-9_-]+)\s+' +            # File group [5]
            r'(\d+)\s+' +                       # File size in bytes [6]
            r'(\w{3}\s+\d{1,2})\s+' +           # 3-char month and 1/2-char day of the month [7]
            r'(\d{1,2}:\d{1,2}|\d{4})\s+' +     # Time or year (need to check conditions) [+= 7]
            r'(.+)$',                           # File/directory name [8]
            line
        )

        date = parts[7]
        time = parts[8] if ':' in parts[8] else '00:00'
        year = parts[8] if ':' not in parts[8] else current_year
        dt_obj = parser.parse("%s %s %s" % (date, year, time))

        files.append({
            'directory': parts[1],
            'perms': parts[2],
            'items': parts[3],
            'owner': parts[4],
            'group': parts[5],
            'size': int(parts[6]),
            'date': date,
            'time': time,
            'year': year,
            'name': parts[9],
            'datetime': dt_obj
        })
    return files


if __name__ == '__main__':
    ftp = jcFtp('ftp2.datasus.gov.br', 'anonymous', 'anon@anon.com')
    ftp.cd('/public/sistemas/tup/downloads/')
    #ftp.get('TabelaUnificada_202103_v2103031426.zip', 'TabelaUnificada_202103.zip')
    files = ftp.list()

    for file in files:
        if 'TabelaUnificada_202103' in file:
            print(file)
            ftp.get(file, 'TabelaUnificada_202103.zip')

    ftp.close()
