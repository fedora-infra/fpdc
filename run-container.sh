#!/bin/bash

echo ">> Waiting for postgres to start"
WAIT=0
while ! psql -h 127.0.0.1 postgres postgres -c "select 1"; do
    sleep 1
    WAIT=$(($WAIT + 1))
    if [ "$WAIT" -gt 15 ]; then
        echo "Error: Timeout wating for Postgres to start"
        exit 1
    fi
done

django-admin migrate
echo "The server is now available at http://127.0.0.1:8000"
django-admin runserver 0.0.0.0:8000
