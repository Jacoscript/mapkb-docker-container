FROM tomcat:9.0.30-jdk11-openjdk
ENV tomcat_dir /usr/local/tomcat
ENV tomcat_bin $tomcat_dir/bin
ENV webapps /usr/local/tomcat/webapps

# Install Maven
RUN apt-get update && apt-get install maven p7zip-full -y; \
    mv  $webapps.dist/* $webapps; \
    mkdir /root/.ssh; \ 
   echo 'StrictHostKeyChecking no' >> /root/.ssh/config
COPY .ssh/* /root/.ssh/
# Copy over any deployment scripts
COPY deployment_scripts /deployment_scripts
RUN chmod 600 /root/.ssh/*
COPY karma /root/karma
COPY /jar/marmotta584.war $webapps/marmotta.war



RUN chmod -R a+x /deployment_scripts; \  
    chmod -R a-x /deployment_scripts/readme.txt; \
    for i in `ls /deployment_scripts`; do if [ -x /deployment_scripts/$i ]; then /deployment_scripts/$i; fi; done; \
    rm -rf /deployment_scripts/; \
    wget -O geoserver.zip http://sourceforge.net/projects/geoserver/files/GeoServer/2.16.0/geoserver-2.16.0-war.zip; \
    unzip geoserver.zip -d geoserver; \
    mv geoserver/geoserver.war $webapps; \
    rm geoserver.zip; \
    rm -rf geoserver/; \
    git clone  https://github.com/tpehle/karma4marmotta /karma4marmotta; \ 
    mv /karma4marmotta/src/ui/usgs/ /usr/local/tomcat/webapps

# Install OpenJDK 8 and Marmotta
#RUN sh -c "cd /opt; wget https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u242-b08/OpenJDK8U-jdk_x64_linux_hotspot_8u242b08.tar.gz; tar xvf OpenJDK8U-jdk_x64_linux_hotspot_8u242b08.tar.gz; rm OpenJDK8U-jdk_x64_linux_hotspot_8u242b08.tar.gz"
#RUN for i in `ls /etc/ssl/certs | grep "pem\|crt"`; do echo y | /opt/jdk8u242-b08/bin/keytool -import -trustcacerts -keystore /opt/jdk8u242-b08/jre/lib/security/cacerts -alias $i -storepass changeit -file /etc/ssl/certs/$i; done
#RUN sh -c "cd /; git clone https://github.com/apache/marmotta.git; cd /marmotta; git checkout MARMOTTA-584; JAVA_HOME=/opt/jdk8u242-b08 mvn clean install -Dmaven.test.skip=true; cd launchers/marmotta-webapp; JAVA_HOME=/opt/jdk8u242-b08 mvn package"


# Clone asset repo and copy .war files to webapps folder
RUN git clone git@code.chs.usgs.gov:cegis/makb_assets.git /makb_assets; \
    mv /makb_assets/archives/*.war $webapps

# Make scripts executable
RUN chmod a+x /makb_assets/scripts/*; \
    cd /makb_assets && /makb_assets/scripts/download.sh; \
    for i in `ls /root/.ssh`; do if [ $i != 'config' ]; then rm /root/.ssh/$i; fi; done

# Clean up
RUN rm -rf /karma4marmotta