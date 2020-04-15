#!/bin/sh

NEW_TAG=$1
CC_TYPE=$2 # fix, feat, chore, test, docs, ...
COMMIT_MSG=$3

DOCKER_HUB="zechery/bitfront-price-alert"
NEW_IMAGE="$DOCKER_HUB:$NEW_TAG"

# commit
echo -e "Commit and push to Git '$CC_TYPE: $COMMIT_MSG'\n"
git commit -am "$CC_TYPE: $COMMIT_MSG"
git push origin master

# tag
echo -e "Add and push a tag $NEW_TAG: $COMMIT_MSG\n"
git tag -a "$NEW_TAG" -m "$NEW_TAG: $COMMIT_MSG"
git push origin "$NEW_TAG"

# docker build & push
echo -e "Build new Docker image $NEW_IMAGE\n"
docker build -t "$NEW_IMAGE" .
echo -e "Push new Docker image $NEW_IMAGE\n"
docker push "$NEW_IMAGE"
