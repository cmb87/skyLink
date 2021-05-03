FROM node:alpine3.13

MAINTAINER christian.peeren@gmail.com

RUN mkdir /home/node/app

WORKDIR /home/node/app

#COPY dist/demoapp /home/node/app/
COPY app /home/node/app

RUN chown -R node /home/node/app/

USER node

RUN npm ci
EXPOSE 5000

CMD ["node", "app.js"]
