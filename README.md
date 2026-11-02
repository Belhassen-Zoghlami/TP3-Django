git clone
python -m venv .envy
.\.envy\Scripts\activate
python -m pip install -r requirements.txt
if needed: (python -m pip install --upgrade pip)
python manage.py migrate
python manage.py runserver
