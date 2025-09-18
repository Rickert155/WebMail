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


def WebMail(login_config:str=None):
    iniMailer()
    
    list_base = ListBase()

    try:
        driver = LoginWebMail(login_config=login_config)
        if driver != None:
            """
            SendMessage(
                    driver, 
                    recipient="@gmail.com",
                    subject="",
                    message="Hello!"
                    )
            """
            pass
        else:
            sys.exit(f'{RED}driver = None{RESET}')

    except Exception as err:
        sys.exit(f'{RED}Error: {err}{RESET}')

    finally:
        try:
            if driver != None:
                driver.quit()
        except UnboundLocalError:
            pass

if __name__ == '__main__':
    params = sys.argv
    if len(params) == 1:
        WebMail()
    elif len(params) == 3 and '--config' in params[1] and '.json' in params[2]:
        login_config = params[2]
        if os.path.exists(login_config):
            WebMail(login_config=login_config)
        else:
            print(f'{RED}Файл конфигурации {login_config} не обнаружен{RESET}')
            helper()
    elif '--help' in params:
        helper()
    else:
        helper()
