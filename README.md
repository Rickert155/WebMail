# WebMail - рассыльщик писем

## Цель проекта
Инструмент решает задачу автоматической рассылки писем через WebMail(веб-интерфейс roundcube)

## Установка
Клонируем репозиторий
```sh
git clone <url>/WebMail.git
```
Ставим модули
```sh
cd WebMail && python3 -m venv venv && ./venv/bin/pip install -r package.txt
```

## Данные для запуска рассылки
### Data/login.json
Можете копировать темплейт и заполнить вашими даннымы для авторизации. 
```sh
cp Data/template_login.json Data/login.json
```

