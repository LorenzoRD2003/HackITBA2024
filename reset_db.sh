cd hackitba_2024
rm ./db.sqlite3
rm ./exercises/migrations/0001_initial.py
rm ./user_auth/migrations/0001_initial.py
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell < populate_db.py