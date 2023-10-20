db:
	python3 src/backend/humalect_weather_app/manage.py makemigrations
	python3 src/backend/humalect_weather_app/manage.py migrate

backend:
	make db
	python3 src/backend/humalect_weather_app/manage.py runserver

frontend:
	npm run dev --prefix ./src/frontend/humalect-weather-app/