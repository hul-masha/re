#!/bin/bash

echo "DEPLOYING WEB"

sed -i -e 's/\r$//' docker/install-python-libs.sh
sed -i -e 's/\r$//' docker/install-system-libs.sh
sed -i -e 's/\r$//' docker/release-web.sh
sed -i -e 's/\r$//' docker/run-beat.sh
sed -i -e 's/\r$//' docker/run-web.sh
sed -i -e 's/\r$//' run-gunicorn.sh

DOCKER_SCRIPTS="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

"${DOCKER_SCRIPTS}/install-system-libs.sh"

"${DOCKER_SCRIPTS}/install-python-libs.sh"

PROJECT_DIR="$(cd "${DOCKER_SCRIPTS}/.." >/dev/null 2>&1 && pwd)"

cd "${PROJECT_DIR}" || exit 1

pipenv --three

make venv

echo "DONE: DEPLOYING WEB"