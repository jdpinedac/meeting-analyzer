#!/bin/sh

# Fix TZ
sudo ln --symbolic --force /usr/share/zoneinfo/"$(curl http://ip-api.com/json/ \
--silent | jq .timezone | tr -d '"')" /etc/localtime

# Install pre-commit
if [ -d "/${WORKDIR}/${PROJ_NAME}/.git" ] && [ -f "/${WORKDIR}/${PROJ_NAME}/.pre-commit-config.yaml" ]; then
    echo "Installing pre-commit"
    pre-commit install
    pre-commit install-hooks
else
    echo "Not installing pre-commit"
fi

exec "$@"
