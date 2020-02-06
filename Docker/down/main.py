#import os
import sys
import wget

def ddl():
    sys.stdout.write('\nStarting download\n') ; sys.stdout.flush()
    url = 'https://raw.githubusercontent.com/lobosor/CSV/master/kc_house_data.csv'
    wget.download(url, '/mnt/WS/data.csv')
    sys.stdout.write('\nFinished download\n') ; sys.stdout.flush()
#    os.write("\nFinished download\n")

ddl()
