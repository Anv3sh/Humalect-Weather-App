FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/backend/humalect_weather_app

COPY requirements.txt /app/backend/humalect_weather_app

# Build psycopg2-binary from source -- add required required dependencies
RUN apk add --virtual .build-deps --no-cache postgresql-dev gcc python3-dev musl-dev && \
        pip install --no-cache-dir -r requirements.txt && \
        apk --purge del .build-deps

COPY --chmod=+x . /app/backend/humalect_weather_app

RUN chmod +x /app/backend/humalect_weather_app/startup.sh

ENTRYPOINT ["/app/backend/humalect_weather_app/startup.sh"]