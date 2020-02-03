#!/bin/bash

MAKB_ASSETS="/makb_assets"
SCRIPTS="$MAKB_ASSETS/scripts"
if [ -e /.is_development ]; then service ssh start; fi

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
        
        # Configure GeoServer
        REST='http://localhost:8080/geoserver/rest/'
        CURL='curl -u admin:geoserver'
        
        $CURL -X POST -H "Content-Type: application/json" -d '{ "namespace": { "prefix": "usgsns", "uri": "http://data.usgs.gov/" } }' $REST/namespaces
        $CURL -X POST -H "Content-Type: application/json" -d '{ "dataStore": { "name": "usgs_prototype_geonames", "description": "shapefiles for the usgs prototype", "connectionParameters": { "entry": [ {"@key":"url","$":"file:/data/shp/geonames"} ] } } }' $REST/workspaces/usgsns/datastores
        $CURL -X POST -H "Content-Type: application/json" -d '{ "dataStore": { "name": "usgs_prototype_gnis", "description": "shapefiles for the usgs prototype", "connectionParameters": { "entry": [ {"@key":"url","$":"file:/data/shp/usgs_layers/gnis"} ] } } }' $REST/workspaces/usgsns/datastores
        $CURL -X POST -H "Content-Type: application/json" -d '{ "dataStore": { "name": "usgs_prototype_structures", "description": "shapefiles for the usgs prototype", "connectionParameters": { "entry": [ {"@key":"url","$":"file:/data/shp/usgs_layers/structures"} ] } } }' $REST/workspaces/usgsns/datastores
        
        # If geoserver url is set, run the export script, oterhwise just use what is in the json data folder
        if [ ! -z ${GEOSERVER_URL+x} ]; then 
            echo "Running Geoserver layer export"
            /makb_assets/scripts/export_geoserver.sh
        fi
        echo "Running Geoserver layer import"
        for i in `ls /makb_assets/json_data`
        do
            $CURL -X POST -H "Content-Type: application/json"  -d @/makb_assets/json_data/$i $REST/workspaces/usgsns/featuretypes
        done

        # Do script imports
        #$SCRIPTS/convert.sh
        #$SCRIPTS/import_marmotta.sh


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
        
        # Disable security in Marmotta
        echo 'security.enabled = false' >> /usr/local/tomcat/webapps/marmotta/system-config.properties

        


        # Setup database
        cat /usr/local/tomcat/webapps/marmotta/system-config.properties | sed 's/ = sa/ = postgres/' | sed -e 's/database.url = .*/database.url = jdbc:postgresql:\/\/makb-docker-container_postgresql_1:5432\/marmotta\ndatabase.type = postgres/' > /usr/local/tomcat/webapps/marmotta/system-config.properties.temp
        mv /usr/local/tomcat/webapps/marmotta/system-config.properties.temp /usr/local/tomcat/webapps/marmotta/system-config.properties


        # Clone the repo if we are not in development
        if [ ! -e /.is_development ]; then 
            git clone git@code.chs.usgs.gov:cegis/makb.git /usr/local/tomcat/webapps/makb
            if [ ! -z ${BRANCH+x} ]; then 
                cd /usr/local/tomcat/webapps/makb
                git checkout $BRANCH 
            fi
        fi

    fi 

fi

exec "$@"