from SinCity.colors import RED, RESET, GREEN

from modules.config import (
        base_dir, 
        data_dir, 
        result_dir, 
        trash_dir,
        users_dir
        )
import csv, os, sys

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
