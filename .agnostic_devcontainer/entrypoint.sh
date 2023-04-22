#!/bin/sh

# Install pre-commit
if [ -d "/${WORKDIR}/${PROJ_NAME}.git" ] && [ -f "/workspaces/.pre-commit-config.yaml" ]; then
    echo "Installing pre-commit"
    pre-commit install
    pre-commit install-hooks
else
    echo "Not installing pre-commit"
fi

# Fix TZ
sudo ln --symbolic --force /usr/share/zoneinfo/"$(curl http://ip-api.com/json/ --silent | jq .timezone | tr -d '"')" /etc/localtime
exec "$@"
