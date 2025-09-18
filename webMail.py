from SinCity.Browser.driver_chrome import driver_chrome
from SinCity.colors import RED, RESET, GREEN

from modules.config import base_dir
from modules.helper import helper
from modules.miniTools import iniMailer, RecordingSendEmail, CheckSendEmail

from modules.send_message import SendMessage
from modules.login import LoginWebMail, getLoginData

import os, sys, csv, time

def ListBase():
    list_base = []
    for base in os.listdir(base_dir):
        if '.csv' in base:list_base.append(f'{base_dir}/{base}')
    return list_base


def WebMail(login_config:str=None):
    iniMailer()
    
    list_base = ListBase()
    if len(list_base) == 0:sys.exit(f'{RED}Нет базы для рассылки!{RESET}')
    
    """Получаем список(множество) завершенных получателей"""
    complite_list_email = CheckSendEmail()

    user_data = getLoginData(login_config=login_config)
    limit = user_data['limit']
    sender = user_data['login']
    
    """Считаем отправленные сообщения за сессию"""
    current_send_mail = 0
    
    """Логинимся в почтовик"""
    driver = LoginWebMail(login_config=login_config)
    
    """Перебираем все базы"""
    for base in list_base:
        with open(base, 'r') as file:
            number_email = 0
            for row in csv.DictReader(file):
                number_email+=1
                company = row['Company']
                email = row['Email']
                try:name = row['Name']
                except:name = None

                """Если только не отправляли ранее этому получателю"""
                if email not in complite_list_email:
                    current_send_mail+=1
                    print(f'[{number_email}] {email} | {name}')
                    
                    """Пишем в док, что отправили"""
                    RecordingSendEmail(
                            email=email, 
                            company=company, 
                            name=name, 
                            base_name=base,
                            sender=sender
                            )
                    time.sleep(1)
                    if limit == current_send_mail:
                        return 


    try:
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
    
    except KeyboardInterrupt:
        sys.exit(f'{RED}\nExit...{RESET}')
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
