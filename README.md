## Описание:
#### Скачиваем репозиторий проекта:
 git clone git@github.com:VladKuzMish/api_final_yatube.git```
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
