FROM node:20-alpine

WORKDIR /app/frontend/

COPY package*.json /app/frontend/
RUN npm i

COPY . /app/frontend/

CMD ["npm", "run", "dev"]