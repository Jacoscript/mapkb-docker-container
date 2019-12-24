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

        # Add LD Cache endpoint
        echo 'ldcache.endpoint.karma\ endpoint\ \ usgs\ wfs.name = Karma Endpoint - USGS WFS' >> /usr/local/tomcat/webapps/marmotta/system-config.properties
        echo 'ldcache.endpoint.karma\ endpoint\ \ usgs\ wfs.prio = 2' >> /usr/local/tomcat/webapps/marmotta/system-config.properties
        echo 'ldcache.endpoint.karma\ endpoint\ \ usgs\ wfs.provider = karma rdf service' >> /usr/local/tomcat/webapps/marmotta/system-config.properties
        echo 'ldcache.endpoint.karma\ endpoint\ \ usgs\ wfs.pattern = http://data.usgs.gov/*' >> /usr/local/tomcat/webapps/marmotta/system-config.properties
        echo 'ldcache.endpoint.karma\ endpoint\ \ usgs\ wfs.service = http://localhost:8080/web-services-rdf-0.0.1-SNAPSHOT/rdf/r2rml/rdf' >> /usr/local/tomcat/webapps/marmotta/system-config.properties
        echo 'ldcache.endpoint.karma\ endpoint\ \ usgs\ wfs.expiry = 240' >> /usr/local/tomcat/webapps/marmotta/system-config.properties
        echo 'ldcache.endpoint.karma\ endpoint\ \ usgs\ wfs.active = true' >> /usr/local/tomcat/webapps/marmotta/system-config.properties
        echo 'ldcache.endpoint.karma\ endpoint\ \ usgs\ wfs.contenttype =' >> /usr/local/tomcat/webapps/marmotta/system-config.properties

        # Setup database - This is currently broken
        cat /usr/local/tomcat/webapps/marmotta/system-config.properties | sed 's/ = sa/ = postgres/' | sed -e 's/database.url = .*/database.url = jdbc:postgresql:\/\/makb-docker-container_postgresql_1:5432\/marmotta\ndatabase.type = postgres/' > /usr/local/tomcat/webapps/marmotta/system-config.properties.temp
        mv /usr/local/tomcat/webapps/marmotta/system-config.properties.temp /usr/local/tomcat/webapps/marmotta/system-config.properties

    fi 

fi

exec "$@"