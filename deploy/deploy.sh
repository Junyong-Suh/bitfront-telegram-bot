#!/bin/sh

CYAN='\033[0;36m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# validate if both git and docker have the same tag
LAST_TAG=$(./get_last_tag.sh) # execute and capture stdout
STATUS=$? # find out exit status
if [ $STATUS -eq 0 ]; then
  printf "${CYAN}Current Git and Docker tag: ${LAST_TAG}${NC}\n"
else
  printf "${LAST_TAG}"
  exit 1
fi

# start deploying
DOCKER_HUB="zechery/bitfront-price-alert"
NEW_IMAGE="$DOCKER_HUB:$LAST_TAG"
printf "${CYAN}Deploy ${NEW_IMAGE}${NC}\n"

# stop and remove current containers
printf "${CYAN}Stop all running containers:${NC}\n"
docker stop "$(docker ps -aq)"
printf "${CYAN}Remove all containers:${NC}\n"
docker rm "$(docker ps -aq)"

# pull and run the new image
printf "${CYAN}Run ${NEW_IMAGE}:${NC}\n"
docker run -d "$NEW_IMAGE"

# done deploying, display images and containers
#printf "${CYAN}Docker images:${NC}\n"
#docker images
printf "${CYAN}Docker containers:${NC}\n"
docker ps
printf "${GREEN}Deployed ${NEW_IMAGE}${NC}\n"