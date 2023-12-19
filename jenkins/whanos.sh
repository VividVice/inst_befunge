#!/bin/bash

LAST_COMMIT=""

if [ "$LAST_COMMIT" != `git log -n 1  | grep commit | awk '{ print $2 }'` ]; then
    echo "new commits appeared need to change image"
    LANGUAGE=$(/var/jenkins_home/getLanguage.sh .)

    if [ $? -eq 1 ]; then
        exit 84
    fi
    if test -f "./Dockerfile"; then
        docker build . -t whanos-project-$1
    else
        docker build . -t whanos-project-$1 -f /images/$LANGUAGE/Dockerfile.standalone
    fi
    docker tag whanos-project-$1 localhost:5000/whanos-project-$1
    docker push localhost:5000/whanos-project-$1
    docker pull localhost:5000/whanos-project-$1
    docker rmi whanos-project-$1

    if test -f "./whanos.yml"; then
        FILE_CONTENT=`cat ./whanos.yml | base64 -w 0`
        curl -H "Content-Type: application/json" -X POST -d "{\"image\":\"localhost:5000/whanos-project-$1\",\"config\":\"$FILE_CONTENT\",\"name\":\"$1\"}" http://localhost:3030/deployments
    fi
    mkdir -p /usr/share/jenkins_hash
fi
