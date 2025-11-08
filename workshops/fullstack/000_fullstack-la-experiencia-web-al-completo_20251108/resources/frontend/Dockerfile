FROM node:22-alpine

WORKDIR /app

# Copia package* para instalar deps
COPY package*.json ./
RUN npm install

# Copia el resto del código
COPY . .

# El build se ejecuta desde el command del servicio en docker-compose
RUN sh -c "npm install && npm run build && cp -r dist/* /dist"