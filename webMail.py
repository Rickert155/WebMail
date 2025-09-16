from selenium.webdriver.common.by import By

from SinCity.Browser.driver_chrome import driver_chrome
from SinCity.colors import RED, RESET, GREEN

from modules.miniTools import iniMailer
from modules.config import base_dir, timeout_click
from modules.login import LoginWebMail

import os, sys, time

def ListBase():
    list_base = []
    for base in os.listdir(base_dir):
        if '.csv' in base:list_base.append(base)
    return list_base

def successSend():
    print(f'{GREEN}Успешная отпарвка{RESET}')

def SendMessage(driver, recipient:str, subject:str, message:str):
    try:
        button_compose = driver.find_element(By.CLASS_NAME, 'compose')
        button_compose.click()
        time.sleep(timeout_click)
    except Exception as err:
        sys.exit(f'{RED}compose не обнаружен{RESET}')
    
    try:
        recipient_fields = driver.find_elements(By.TAG_NAME, 'input')
        if len(recipient_fields) > 0:
            for recipient_field in recipient_fields:
                try:
                    role_combobox = recipient_field.get_attribute('role')
                    autocomplete_list = recipient_field.get_attribute(
                            'aria-autocomplete'
                            )
                    if role_combobox == 'combobox' and autocomplete_list == 'list':
                        recipient_field.send_keys(recipient)
                        time.sleep(timeout_click)
                        break
                except:
                    print(err)
    except:
        sys.exit(f'{RED}ошибка при опредении поля для ввода получателя{RESET}')
    
    try:
        subject_field = driver.find_element(By.ID, 'compose-subject')
        subject_field.send_keys(subject)
        time.sleep(timeout_click)
    except:
        sys.exit(f'{RED}ошибка при обнаружении поля для темы письма{RESET}')

    try:
        message_field = driver.find_element(By.NAME, '_message')
        message_field.send_keys(message)
        time.sleep(timeout_click)
    except:
        sys.exit(
                f'{RED}ошибка при обнаружении поля для ввода сообщения\n'
                f'Необходимо проверить настройки: Настройки -> Создание сообщений'
                f' -> Создавать сообщения в HTML - поставить "никогда"{RESET}')

    try:
        try:
            button = driver.find_element(By.ID, 'rcmbtn111').click()
            successSend()
            time.sleep(timeout_click)
        except:
            pass
        try:
            button = driver.find_element(By.ID, 'rcmbtn111-clone').click()
            successSend()
            time.sleep(timeout_click)
        except:
            pass
    except Exception as err:
        sys.exit(f'{RED}ошибка при поиске/нажитии кнопи отправки письма{RESET}\n{err}')
        


def WebMail():
    iniMailer()
    
    list_base = ListBase()
    print(list_base)

    try:
        driver = LoginWebMail()
        if driver != None:
            for base in list_base:
                pass
        else:
            sys.exit(f'{RED}driver = None{RESET}')
    except Exception as err:
        sys.exit(f'{RED}Error: {err}{RESET}')
        if driver != None:
            driver.quit()

if __name__ == '__main__':
    WebMail()
