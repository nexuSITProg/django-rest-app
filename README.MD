Для создания виртуального окружения 

python -m vevn {название_папки}

Открыть CMD (Command Prompt)

Перейти в папку Scripts 

cd venv\Scripts

Активировать файл activate

Просто прописать команду activate

Для скачивания всех зависимостей надо находится в папке где находится файл requirements.txt

Устанавливаем все зависимости 

pip install -r requirements.txt

Мигрировать базу данных в папке с проектом (myproject)

python manage.py makemigrations
python manage.py migrate

Необходимо запустить сервер

python manage.py runserver