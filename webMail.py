from SinCity.Browser.driver_chrome import driver_chrome
from SinCity.colors import RED, RESET, GREEN

from modules.config import base_dir
from modules.helper import helper
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
                    recipient="@gmail.com",
                    subject="",
                    message="Hello!"
                    )
                
        else:
            sys.exit(f'{RED}driver = None{RESET}')
    except Exception as err:
        sys.exit(f'{RED}Error: {err}{RESET}')
        if driver != None:
            driver.quit()

if __name__ == '__main__':
    params = sys.argv
    if len(params) == 1:
        WebMail()
    elif len(params) > 3 and '--config' in params[1] and '.json' in params[2]:
        login_config = params[2]
        if os.path.exists(login_config):
            WebMail(login_config=login_config)
        else:
            helper()
    elif '--help' in params:
        helper()
    else:
        helper()
