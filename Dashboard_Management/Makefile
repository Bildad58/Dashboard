all:
	git add .
	git commit -m "update"
	git push

stage:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

server:
	python manage.py runserver


venv:
	source caps/Scripts/activate && echo "Virtual environment 'caps' activated."

