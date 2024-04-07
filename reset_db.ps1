cd hackitba_2024
Remove-Item -Path .\db.sqlite3
Remove-Item -Path .\exercises\migrations\0001_initial.py
Remove-Item -Path .\user_auth\migrations\0001_initial.py
python manage.py makemigrations
python manage.py migrate
python manage.py shell < populate_db.py