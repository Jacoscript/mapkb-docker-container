#!/bin/bash

if [ "$1" = 'catalina.sh' ]; then
    if [ -d /marmotta ]; then
        echo "Initializing MAKB, this will take about 60 seconds"
        $1 start
        cat /usr/local/tomcat/logs/catalina.out | grep "Server startup" > /dev/null
        while [ $? -ne 0 ]; do
            echo "Waiting for catalina..."
            sleep 1s
            cat /usr/local/tomcat/logs/catalina.out | grep "Server startup" > /dev/null
        done
        $1 stop
        mv /marmotta/WEB-INF/lib/* /usr/local/tomcat/webapps/marmotta/WEB-INF/lib
        rm -rf /marmotta/WEB-INF
        mv /marmotta/config /usr/local/tomcat/webapps/marmotta
        mv /marmotta/* /usr/local/tomcat/webapps/marmotta
        rmdir /marmotta
    fi 

fi

exec "$@"