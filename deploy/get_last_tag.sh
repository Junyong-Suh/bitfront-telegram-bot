#!/bin/bash

# caveat the only stdout output should be the tag if success
# as the output will be a input to ./deploy.sh script

REPO="https://github.com/Junyong-Suh/bitfront-telegram-bot.git"
LAST_GIT_TAG=$(git ls-remote --tags $REPO | awk '{print $2}' | grep -v '{}' | awk -F"/" '{print $3}' | sort -n -t. -k1,1 -k2,2 -k3,3 | tail -n 1)
#echo "Latest Git Tag: $LAST_GIT_TAG"

REGISTRY="zechery/bitfront-price-alert"
LAST_DOCKER_TAG=$(wget -q https://registry.hub.docker.com/v1/repositories/${REGISTRY}/tags -O -  | sed -e 's/[][]//g' -e 's/"//g' -e 's/ //g' | tr '}' '\n'  | awk -F: '{print $3}' | sort -n -t. -k1,1 -k2,2 -k3,3 | tail -n 1)
#echo "Latest Docker Tag: ${LAST_DOCKER_TAG}"

if [ "$LAST_GIT_TAG" != "$LAST_DOCKER_TAG" ]
then
    echo "Tags on Git and Docker are different. (Git: $LAST_GIT_TAG, Docker: $LAST_DOCKER_TAG)"
    exit 1
else
    echo "$LAST_GIT_TAG"
    exit 0
fi