#!/bin/sh

CYAN='\033[0;36m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Get the latest version tag from Git
REPO="https://github.com/Junyong-Suh/bitfront-telegram-bot.git"
LAST_GIT_TAG=$(git ls-remote --tags $REPO | awk '{print $2}' | grep -v '{}' | awk -F"/" '{print $3}' | sort -n -t. -k1,1 -k2,2 -k3,3 | tail -n 1)
printf "${CYAN}Latest Git Tag ${LAST_GIT_TAG}${NC}\n"

# Build Docker image
DOCKER_HUB="zechery/bitfront-price-alert"
NEW_IMAGE="${DOCKER_HUB}:${LAST_GIT_TAG}"
printf "${CYAN}Building ${NEW_IMAGE}${NC}\n"
docker build -t "$NEW_IMAGE" .
printf "${CYAN}${NEW_IMAGE} created ${NC}\n"

# Push Docker image
printf "${CYAN}Push ${NEW_IMAGE} to Docker Hub${NC}\n"
docker push "$NEW_IMAGE"

printf "${GREEN}Pushed ${NEW_IMAGE} successfully${NC}\n"
