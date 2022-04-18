#!/bin/sh
set -ex

if [[ ! -z "$DEBUG" ]]; then
    export RELOAD="--reload"
fi

uvicorn app.main:app $RELOAD --host 0.0.0.0 --port ${PORT:-8000}
