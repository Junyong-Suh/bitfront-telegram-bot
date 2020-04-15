#!/bin/sh

CYAN='\033[0;36m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# validate if both git and docker have the same tag
LAST_TAG=$(./get_last_tag.sh) # execute and capture stdout
STATUS=$? # find out exit status
if [ $STATUS -eq 0 ]; then
  printf "${CYAN}Current Git and Docker tag: %s${NC}" "$LAST_TAG"
else
  printf "%s" "$LAST_TAG"
  exit 1
fi

# start deploying
DOCKER_HUB="zechery/bitfront-price-alert"
NEW_IMAGE="$DOCKER_HUB:$LAST_TAG"
printf "${CYAN}Deploy %s${NC}" "$NEW_IMAGE"

# stop and remove current containers
printf "${CYAN}Stop all running containers:${NC}"
docker stop "$(docker ps -aq)"
printf "${CYAN}Remove all containers:${NC}"
docker rm "$(docker ps -aq)"

# pull and run the new image
printf "${CYAN}Run $NEW_IMAGE:${NC}"
docker run -d "$NEW_IMAGE"

# done deploying, display images and containers
printf "${CYAN}Docker images:${NC}"
docker images
printf "${CYAN}Docker containers:${NC}"
docker ps
printf "${GREEN}Deployed %s${NC}" "$NEW_IMAGE"