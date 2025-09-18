from SinCity.colors import RED, RESET, GREEN

from modules.config import (
        base_dir, 
        data_dir, 
        result_dir, 
        trash_dir,
        users_dir
        )
import csv, os, sys, time

def iniMailer():
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        sys.exit(f'{RED}Загрузите базу в директорию {base_dir}{RESET}')
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    if not os.path.exists(trash_dir):
        os.makedirs(trash_dir)
    if not os.path.exists(users_dir):
        os.makedirs(users_dir)

def CheckSendEmail():
    list_email = set()
    
    list_base_file = os.listdir(result_dir)
    if len(list_base_file) != 0:    
        for base in os.listdir(result_dir):
            with open(f'{result_dir}/{base}', 'r') as file:
                for row in csv.DictReader(file):
                    try:
                        email = row['Email']
                        list_email.add(email)
                    except:pass

    return list_email

def RecordingSendEmail(
        base_name:str, 
        email:str, 
        company:str, 
        sender:str, 
        name:str=None):
    
    if base_dir in base_name:base_name = base_name.split(base_dir)[1]
    result_base = f'{result_dir}/{base_name}'
    if not os.path.exists(result_base):
        with open(result_base, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Email', 'Company', 'Name', 'Sender', 'Time'])
    
    with open(result_base, 'a+') as file:
        
        current_time = time.strftime('%d/%m/%Y %H:%M:%S')
        
        write = csv.writer(file)
        write.writerow([email, company, name, sender, current_time])

