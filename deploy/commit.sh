#!/bin/sh

CYAN='\033[0;36m'
#GREEN='\033[0;32m'
NC='\033[0m' # No Color

NEW_TAG=$1
CC_TYPE=$2 # fix, feat, chore, test, docs, ...
COMMIT_MSG=$3

#DOCKER_HUB="zechery/bitfront-price-alert"
#NEW_IMAGE="$DOCKER_HUB:$NEW_TAG"

# commit
printf "${CYAN}Commit and push to Git ${CC_TYPE}: ${COMMIT_MSG} ${NC}\n"
git commit -am "$CC_TYPE: $COMMIT_MSG"
git push origin master

# tag
printf "${CYAN}Add and push a tag ${NEW_TAG}: ${COMMIT_MSG}${NC}\n"
git tag -a "$NEW_TAG" -m "$NEW_TAG: $COMMIT_MSG"
git push origin "$NEW_TAG"

# docker build & push
#printf "${CYAN}Build new Docker image ${NEW_IMAGE}${NC}\n"
#docker build -t "$NEW_IMAGE" .
#printf "${CYAN}Push new Docker image ${NEW_IMAGE}${NC}\n"
#docker push "$NEW_IMAGE"
#
#printf "${GREEN}Completed successfully${NC}\n"