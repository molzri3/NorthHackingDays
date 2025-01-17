#!/bin/bash
docker rm -f ho9na
docker build --no-cache --tag=ho9na .
docker run -p 1337:8080 --rm --name=ho9na -it ho9na
