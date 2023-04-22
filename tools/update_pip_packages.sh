#!/usr/bin/env bash
python3 -m pip install --upgrade pip
python3 -m pip install ansible boto3 checkov pip_audit pre-commit
python3 -m pip freeze > ../.agnostic_devcontainer/requirements.txt
