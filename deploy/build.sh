#!/bin/bash

host=192.168.0.11
# host=localhost

echo "Building images"
docker build -q -t skivrige.writing/nginx nginx
docker build -q -t skivrige.writing/backend ../backend
docker build -q -t skivrige.writing/frontend ../frontend

echo "Tagging images"
docker tag skivrige.writing/nginx $host:5000/skivrige.writing/nginx
docker tag skivrige.writing/backend $host:5000/skivrige.writing/backend
docker tag skivrige.writing/frontend $host:5000/skivrige.writing/frontend

echo "Pushing images"
docker push $host:5000/skivrige.writing/nginx
docker push $host:5000/skivrige.writing/backend
docker push $host:5000/skivrige.writing/frontend