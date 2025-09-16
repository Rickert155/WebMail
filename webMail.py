from SinCity.Browser.driver_chrome import driver_chrome
from modules.miniTools import iniMailer
from modules.config import base_dir
import os

def ListBase():
    list_base = []
    for base in os.listdir(base_dir):
        if '.csv' in base:list_base.append(base)
    return list_base

def WebMail():
    iniMailer()

    list_base = ListBase()
    print(list_base)

if __name__ == '__main__':
    WebMail()
