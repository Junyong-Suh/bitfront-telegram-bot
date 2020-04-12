#!/bin/sh

# validate if both git and docker have the same tag
LAST_TAG=$(./get_last_tag.sh) # execute and capture stdout
STATUS=$? # find out exit status
if [ $STATUS -eq 0 ]; then
  echo "Current Git and Docker tag: $LAST_TAG"
else
  echo "$LAST_TAG"
  exit 1
fi

# start deploying
DOCKER_HUB="zechery/bitfront-price-alert"
NEW_IMAGE="$DOCKER_HUB:$LAST_TAG"
echo "Deploy $NEW_IMAGE"

# stop and remove current containers
echo "Stop all running containers:"
docker stop "$(docker ps -aq)"
echo "Remove all containers:"
docker rm "$(docker ps -aq)"

# pull and run the new image
echo "Run $NEW_IMAGE:"
docker run -d "$NEW_IMAGE"

# done deploying, display images and containers
echo "Docker images:"
docker images
echo "Docker containers:"
docker ps
echo "Deployed $NEW_IMAGE"