#!/bin/bash
docker-compose pull
docker-compose down
git pull
docker-compose up -d