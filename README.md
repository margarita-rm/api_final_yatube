## Описание:
Api_final_yatube - это REST API для блога Yatube, с его помощью можно зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

## Cтек используемых технологий:
Python, GitHub, VSCode, Django, REST API, JWT, OpenAPI

## Установка:
#### Скачиваем репозиторий проекта:
git clone git@github.com:margarita-rm/api_final_yatube.git
#### Создаем виртуальное окружение:
python -m venv venv
#### Активируем виртуальное окружение: 
source venv/Scripts/activate
#### Устанавливаем зависимости из файла requirements.txt:
python -m pip install --upgrade pip

pip install -r requirements.txt
#### Выполняем миграции:
python manage.py migrate
#### Запускаем проект:
python manage.py runserver

## Примеры запросов к API:
#### Запрос JWT токена с использованием логина и пароля пользователя Admin:
  [POST].../api/v1/jwt/create/
  
{
  
    "username": "Admin",
    
    "password": "Changeme1!"
    
}
#### Ответ:
{

"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MjA5NTYwNywianRpIjoiMDBmMGI0MG.sE5Bd3vrnQLIAL5GxxFg36tPoYyB9I5MQBE_iGshpK4",
 
 "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMDk1NjA3LCJqdGkiOiI0YmIxN2MzODcwNGU0YzQ0OWQ4Nzg4NzA4ODcyZTliMCIsInVzZXJfaWQiOjF9"

}

#### Автор:
Маргарита Мифтахова
