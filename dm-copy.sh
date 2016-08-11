#!/bin/bash

echo "copying..."

docker-machine scp -r $2/. docker@$1:~/tmp/
docker-machine ssh $1 sudo cp -a tmp/* $3
docker-machine ssh $1 rm -rf ~/tmp/*

echo "done copying"
