#!/bin/bash
set -e

echo "$1"

if [ "$1" = 'catalina.sh' ]; then
    if [ -d /marmotta ]; then
        echo "Initializing MAKB, this will take about 60 seconds"
        $1 start
        sleep 30s
        $1 stop
        mv /marmotta/WEB-INF/lib/* /usr/local/tomcat/webapps/marmotta/WEB-INF/lib
        rm -rf /marmotta/WEB-INF
        mv /marmotta/config /usr/local/tomcat/webapps/marmotta
        mv /marmotta/* /usr/local/tomcat/webapps/marmotta
        rmdir /marmotta
        sleep 10s
    fi 

fi

exec "$@"