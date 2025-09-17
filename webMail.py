from SinCity.Browser.driver_chrome import driver_chrome
from SinCity.colors import RED, RESET, GREEN

from modules.config import base_dir
from modules.miniTools import iniMailer

from modules.send_message import SendMessage
from modules.login import LoginWebMail

import os, sys

def ListBase():
    list_base = []
    for base in os.listdir(base_dir):
        if '.csv' in base:list_base.append(base)
    return list_base


def WebMail():
    iniMailer()
    
    list_base = ListBase()
    print(list_base)

    try:
        driver = LoginWebMail()
        if driver != None:
            SendMessage(
                    driver, 
                    recipient="maksimnegulyaev@gmail.com",
                    subject="Subject to max",
                    message="Hello, Max!"
                    )
                
        else:
            sys.exit(f'{RED}driver = None{RESET}')
    except Exception as err:
        sys.exit(f'{RED}Error: {err}{RESET}')
        if driver != None:
            driver.quit()

if __name__ == '__main__':
    WebMail()
