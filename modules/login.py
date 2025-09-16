from selenium.webdriver.common.by import By

from SinCity.Browser.driver_chrome import driver_chrome
from SinCity.colors import RED, RESET, GREEN

from modules.config import data_login
from modules.config import timeout_login

import json, os, time, sys

def getLoginData():
    if os.path.exists(data_login):
        with open(data_login, 'r') as file:
            data = json.load(file)
            
            auth_data = {
                    "login":data['login'],
                    "password":data['password'],
                    "url_login":data['url']
                    }
            return auth_data

    if not os.path.exists(data_login):
        sys.exit(f'{RED}Добавь {data_login}{RESET}')

def checkCaptcha(driver):
    page_source = driver.page_source
    if 'Cloudflare' in page_source:
        return True
    else:
        return False

def auth_web_mail(login:str, password:str, url:str):
    driver = None
    try:
        driver = driver_chrome()
        driver.get(url)
        time.sleep(3)

        captcha = checkCaptcha(driver)
        if captcha == True:
            return 'Captcha'
        if captcha == False:
            
            try:
                print(f'login:\t\t{login}')
                login_field = driver.find_element(By.ID, 'rcmloginuser')
                login_field.send_keys(login)
                time.sleep(timeout_login)
            except Exception as err_login:
                sys.exit(f'{RED}Ошибка при вводе логина\n{err_login}{RESET}')

            try:
                censurship_password = '*'*len(password)
            
                print(f'password:\t{censurship_password}')
                password_field = driver.find_element(By.ID, 'rcmloginpwd')
                password_field.send_keys(password)
                time.sleep(timeout_login)
            except Exception as err_password:
                sys.exit(f'{RED}Ошибка при вводе пароля\n{err_password}{RESET}')

            try:
                button_login = driver.find_element(By.ID, 'rcmloginsubmit')
                button_login.click()
                time.sleep(timeout_login)
            except Exception as err_button:
                sys.exit(f'{RED}Ошибка при нажатии на кнопку\n{err_button}{RESET}')
        
        return 'OK'

    except KeyboardInterrupt:
        sys.exit(f'{RED}\nExit...{RESET}')

    except Exception as err:
        print(
                f'{RED}Авторизация не пройдена!{RESET}\n'
                f'Error: {err}'
                )
    finally:
        if driver != None:
            driver.quit()

def LoginWebMail():
    auth_data = getLoginData()
    
    login = auth_data['login']
    password = auth_data['password']
    url_login = auth_data['url_login']

    print(f'url:\t\t{url_login}')
    
    login_state = False
    count_login, max_count_login = 0, 3
    while login_state != True:
        count_login+=1
        auth = auth_web_mail(login=login, password=password, url=url_login)
        if auth == 'Captcha':
            print(
                    f'{RED}[{count_login}/{max_count_login}] '
                    f'Обнаружена проверка анти-бот!{RESET}'
                    )
        if auth == 'OK':
            login_state = True
            print(f'{GREEN}Авторизация прошла успешно{RESET}')

        if count_login == max_count_login:
            break

if __name__ == '__main__':
    LoginWebMail()
