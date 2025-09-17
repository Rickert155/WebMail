from SinCity.colors import RED, RESET, GREEN, BLUE
from modules.create_message import helpCreateMessage

def helpStartWebMail():
    text = f"""\
    {BLUE}<Авторизация>{RESET}{RED}
    Для запуска рассыльщика используются файлы конфигурации для авторизации
    По умолчанию используется конфиг Data/login.json
    Если его нет - его необходимо создать или копировать шаблон:
    
    cp Data/template_login.json Data/login.json

    Возможно передать альтернативный путь до файла конфигурации:
    
    python3 webMail.py --config other.json
    {RESET}\
    """
    print(text)

def helper():
    helpStartWebMail()
    helpCreateMessage()
