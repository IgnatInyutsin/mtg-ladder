FROM node:16
WORKDIR /usr/src/app/
COPY ./frontend/package*.json ./
RUN npm install -g @angular/cli @angular-devkit/build-angular && npm install && npm rebuild node-sass
EXPOSE 4200
CMD ["npm", "start"]