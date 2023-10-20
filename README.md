# Humalect-Weather-App:

- This is a Django+React weather app that uses the `Accuweather` api at the backend to fetch weather and forecast data for the given city name.

- The application also implements an autocomplete feature where given an incomplete city name the api finds the closest city name and gives the data for it. AccuWeather's `Autocomplete api` is used for this with some added checks.

- The application also stores the Cities searched for in the PostgreSQL db in order to save api calls. In order to update the saved data over time the application implements a cron job through which it can schedule a db updation job every 1 hour for both weather data and forecast data.

- The app also generates a chart of temperature over time using the 12 hrs forecast data of a city.
- The app follows a modular structure.

## Local setup:

- Setup `.env` in `./src/backend/humalect_weather_app` and `./src/frontend/humalect-weather-app`

`./src/backend/humlect_weather_app/.env`:
```
ACCUWEATHER_API_KEY = <your-key>
ACCUWEATHER_BASE_URL = http://dataservice.accuweather.com
```
`./src/frontend/humalect-weather-app/.env`:
```
VITE_REACT_APP_BACKEND_API_ENDPOINT = http://localhost:8000/humalect-weather-api/v1
```

- To run backend type the following command in the root dir:
```
make backend
```
- To run frontend type the following command in the root dir:
```
make frontend
```

## Cron Job:
The cron command-line utility is a job scheduler on Unix-like operating systems.
In this application the updation of city data is handled through a `cron` job which is established through custom Django management command namely `scheduler`.

To run the cron job type following in the root dir
```
make run cron
```

A python library named `schedule` is used for this.
## Docker Compose:

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services. Then, with a single command, you create and start all the services from your configuration.

Compose works in all environments; production, staging, development, testing, as well as CI workflows. It also has commands for managing the whole lifecycle of your application:

- Start, stop, and rebuild services
- View the status of running services
- Stream the log output of running services
- Run a one-off command on a service

Here we have 3 services the Django backend, React frontend and PostgreSQL database.
What if we could containerse them and run together yet isolated from each other. Well docker-compose can do that for you.

### Steps:
Write these commands in the root dir:

```
docker-compose build
```
`docker-compose build` builds the images for the listed services in the `docker-compose.yml` file, here they will be backend, frontend and db.

```
docker compose up
```
`docker compose up` creates the respective containers from the images of the services and composes them together also creating a local network for them in order for the services to communicate.

```
docker compose down
```
`docker compose down` command will stop running containers, but it also removes the stopped containers as well as any networks that were created.

### DB Persistence:

- The DB persistence is maintained through docker volumes where docker attaches a local volume to the DB service so as to have backup data in case the container is closed say through `docker compose down`.

# Challenges faced:

## 1) Implementing Session based weather data:
- Tried implementing a session based city weather data response where I tried to use Django Session which provides a `django_session` table and `Session` model respectively.
- Created a CustomSession model overlapping the Django Session model and created a ManyToMany relationship with the City model.
- This seemed to work fine when the backend api was directly called from the browser, but on being call from the frontend Django had no idea about the session as Javascript has no control over sessions and does not sends one to the backend it is always handled by a server language.
- Tried sending request with `credentials` header but that didn't work too so I had to leave the idea.

## 2) Docker-Compose:
- While i was trying to docker compose the 3 services I faced the issue of the `package.json` for frontend and `manage.py` for backend not being found.
- The Db seemed running fine with no errors.
## 3) Creating a package out of the backend:
- Tried creating a package out of the backend in order to remove any unnecessary import errors and smooth functioning of the backend api.
- Created a `pyproject.toml` file and added build dependencies added a run script in the `__init__.py` but didn't seem to work.