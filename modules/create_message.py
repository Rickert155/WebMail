from SinCity.colors import RED, RESET, BLUE, GREEN

import sys

def helpCreateMessage():
    text = f"""\
    {BLUE}<Тестирование создания письма>{RESET}{RED}
    Необходимо передать два параметра:
    Первым параметром Тему письма
    Вторым параметром Тело письма

    Пример:
    python3 -m modules.create_message 'это тема' 'Это тело письма'

    Возможно передать переменные:
    [COMPANY NAME] [NAME]
    Пример:
    python3 -m modules.create_message 'Hello, [NAME]' 'Testing message to [COMPANY NAME]'
    {RESET}\
    """
    print(text)

TEMPLATE_COMPANY_NAME = '[COMPANY NAME]'
TEMPLATE_NAME = '[NAME]'

def CreateSubject(subject:str, company:str=None, name:str=None):
    if TEMPLATE_COMPANY_NAME in subject:
        subject = subject.replace(TEMPLATE_COMPANY_NAME, company)
    if TEMPLATE_NAME in subject:subject = subject.replace(TEMPLATE_NAME, name)
    return subject

def CreateMessage(message:str, company:str=None, name:str=None):
    if TEMPLATE_COMPANY_NAME in message:
        message = message.replace(TEMPLATE_COMPANY_NAME, company)
    if TEMPLATE_NAME in message:message = message.replace(TEMPLATE_NAME, name)
    return message

if __name__ == '__main__':
    params = sys.argv
    if len(params) == 3:
        subject = params[1]
        message = params[2]

        generateSubject = CreateSubject(
                subject=subject, 
                company="SinCity",
                name="Rickert"
                )
        generateMessage = CreateMessage(
                message=message,
                company="SinCity",
                name="Rickert"
                )
        print(
                f'{RED}{subject}{RESET}\n{GREEN}{generateSubject}{RESET}\n\n'
                f'{RED}{message}{RESET}\n{GREEN}{generateMessage}{RESET}\n'
                )

        
    
    if len(params) != 3:
        helpCreateMessage()
