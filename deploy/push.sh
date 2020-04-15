#!/bin/sh

NEW_TAG=$1
CC_TYPE=$2 # fix, feat, chore, test, docs, ...
COMMIT_MSG=$3

DOCKER_HUB="zechery/bitfront-price-alert"
NEW_IMAGE="$DOCKER_HUB:$NEW_TAG"

#echo "$CC_TYPE: $COMMIT_MSG"
#echo "$NEW_TAG: $COMMIT_MSG"
#echo "$NEW_IMAGE"

# commit
git commit -am "$CC_TYPE: $COMMIT_MSG"
git push origin master

# tag
git tag -a "$NEW_TAG" -m "$NEW_TAG: $COMMIT_MSG"
git push origin "$NEW_TAG"

# docker build & push
docker build -t "$NEW_IMAGE" .
docker push "$NEW_IMAGE"
