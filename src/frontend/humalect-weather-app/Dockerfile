FROM node:20-alpine

WORKDIR /app/frontend/humalect-weather-app

COPY package*.json /app/frontend/humalect-weather-app
RUN npm i
RUN chown -R node /app/frontend/humalect-weather-app/node_modules

COPY . /app/frontend/humalect-weather-app

CMD ["npm", "run", "dev"]