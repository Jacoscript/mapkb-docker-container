FROM tomcat:9.0.30-jdk11-openjdk
ENV tomcat_dir /usr/local/tomcat
ENV tomcat_bin $tomcat_dir/bin
ENV webapps /usr/local/tomcat/webapps

# Install Maven
RUN apt-get update && apt-get install maven -y
RUN mv  $webapps.dist/* $webapps
RUN mkdir /root/.ssh
RUN echo 'StrictHostKeyChecking no' >> /root/.ssh/config
COPY .ssh/* /root/.ssh/
RUN chmod 600 /root/.ssh/*
COPY karma /root/karma

# Copy over any deployment scripts
COPY deployment_scripts /deployment_scripts
RUN chmod -R a+x /deployment_scripts
RUN chmod -R a-x /deployment_scripts/readme.txt
RUN for i in `ls /deployment_scripts`; do if [ -x /deployment_scripts/$i ]; then /deployment_scripts/$i; fi; done
RUN rm -rf /deployment_scripts/

# Install GeoServer
RUN wget -O /geoserver.tar.gz https://github.com/geoserver/geoserver/archive/2.16.0.tar.gz; 
RUN tar xvf /geoserver.tar.gz -C /; mvn clean install -f /geoserver-2.16.0/src -am -Dmaven.test.skip=true
RUN mv /geoserver-2.16.0/src/web/app/target/geoserver.war $webapps

# Install Karma
RUN git clone https://github.com/usc-isi-i2/Web-Karma /Web-Karma; cat /Web-Karma/pom.xml | sed "s/http:\/\/repo1./https:\/\/repo1./g" > /Web-Karma/pomnew.xml; mv /Web-Karma/pomnew.xml /Web-Karma/pom.xml; mvn clean install -f /Web-Karma/pom.xml -Dmaven.test.skip=true; cp /Web-Karma/karma-web/target/karma-web-0.0.1-SNAPSHOT.war $webapps; cp /Web-Karma/karma-web-services/web-services-rdf/target/web-services-rdf-0.0.1-SNAPSHOT.war $webapps 
RUN git clone  https://github.com/tpehle/karma4marmotta /karma4marmotta; mv /karma4marmotta/src/ui/usgs/ /usr/local/tomcat/webapps

# Install OpenJDK 8 and Marmotta
#RUN sh -c "cd /opt; wget https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u242-b08/OpenJDK8U-jdk_x64_linux_hotspot_8u242b08.tar.gz; tar xvf OpenJDK8U-jdk_x64_linux_hotspot_8u242b08.tar.gz; rm OpenJDK8U-jdk_x64_linux_hotspot_8u242b08.tar.gz"
#RUN for i in `ls /etc/ssl/certs | grep "pem\|crt"`; do echo y | /opt/jdk8u242-b08/bin/keytool -import -trustcacerts -keystore /opt/jdk8u242-b08/jre/lib/security/cacerts -alias $i -storepass changeit -file /etc/ssl/certs/$i; done
#RUN sh -c "cd /; git clone https://github.com/apache/marmotta.git; cd /marmotta; git checkout MARMOTTA-584; JAVA_HOME=/opt/jdk8u242-b08 mvn clean install -Dmaven.test.skip=true; cd launchers/marmotta-webapp; JAVA_HOME=/opt/jdk8u242-b08 mvn package"
COPY /jar/marmotta584.war $webapps/marmotta.war


# Clone asset repo
#--- Disabled for development --- RUN git clone git@code.chs.usgs.gov:cegis/makb_assets.git /makb_assets

# Only doing this to save time during development because cloning takes forever
COPY makb_assets /makb_assets

# Make scripts executable
RUN chmod a+x /makb_assets/scripts/*

# Download data
RUN cd /makb_assets && /makb_assets/scripts/download.sh

# Remove any keys
RUN for i in `ls /root/.ssh`; do if [ $i != 'config' ]; then rm /root/.ssh/$i; fi; done