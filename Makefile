db:
	python3 src/backend/humalect_weather_app/manage.py makemigrations
	python3 src/backend/humalect_weather_app/manage.py migrate

backend:
	pip install -r src/backend/humalect_weather_app/requirements.txt
	make db
	python3 src/backend/humalect_weather_app/manage.py runserver

run cron:
	python3 src/backend/humalect_weather_app/manage.py scheduler

frontend:
	npm i --prefix ./src/frontend/humalect-weather-app/
	npm run dev --prefix ./src/frontend/humalect-weather-app/