# Creates an image to run MAKB Tomcat server
# WAR FILES ARE TOO LARGE TO STORE IN GITLAB
# IF PROBLEMS COULD BE RESOLVED WITH GITHUB AND MAVEN ON LOCAL WORKSTATIONS
# THIS SCRIPT COULD BE MODIFIED TO BUILD THEM FROM SOURCE
# !!!! .war, .jar and /usgs files must be added to the Dockerbuild folder !!!!

FROM tomcat:9.0.30-jdk11-openjdk
ENV karma karma-web-0.0.1-SNAPSHOT
ENV tomcat_dir /usr/local/tomcat
ENV tomcat_bin $tomcat_dir/bin
ENV webapps /usr/local/tomcat/webapps
ENV marmotta_dir /marmotta
ENV marmotta_config_dir $marmotta_dir/config
ENV jar jar

# Install Maven
RUN apt-get update && apt-get install maven openssh-server -y

# Create a user called tomcat with password s3cret to access manager/html
COPY 'tomcat-users.xml' '/usr/local/tomcat/conf'

# Let all hosts (including local machine) access the manager
RUN mkdir -p '/usr/local/tomcat/conf/Catalina/localhost'
COPY 'manager.xml' '/usr/local/tomcat/conf/Catalina/localhost'

# Deploy requisite war files 
COPY $jar/geoserver.war $webapps
COPY $jar/marmotta.war $webapps
COPY $jar/$karma.war $webapps 
COPY $jar/web-services-rdf-0.0.1-SNAPSHOT.war $webapps

# Deploy USGS Karma4Marmotta
RUN mkdir $webapps/usgs
COPY $jar/usgs $webapps/usgs

# Configure Tomcat
RUN echo 'export MARMOTTA_HOME=/usr/local/tomcat/webapps/marmotta' > $tomcat_bin/setenv.sh 
RUN echo 'CATALINA_PID="$CATALINA_BASE/bin/catalina.pid"' >> $tomcat_bin/setenv.sh
RUN echo 'export JAVA_OPTS="-Djava.net.preferIPv4Stack=true -Xmx4096m -XX:PermSize=128m -XX:MaxPermSize=256m -XX:+UseConcMarkSweepGC -XX:+CMSClassUnloadingEnabled -XX:+UseConcMarkSweepGC -XX:+HeapDumpOnOutOfMemoryError"' >> $tomcat_bin/setenv.sh
RUN echo 'export MAVEN_OPTS="-Xmx4096m -XX:MaxPermSize=128m"' >> $tomcat_bin/setenv.sh
RUN echo 'export KARMA_USER_HOME=/usr/local/tomcat/karma' >> $tomcat_bin/setenv.sh

# Configure SSH
RUN echo "root:toor" | chpasswd
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

RUN mkdir $webapps/karma
COPY $jar/python $webapps/karma
COPY $jar/preloaded-ontologies $webapps/karma
RUN mkdir /data
COPY $jar/data /data

# Configure Marmotta
RUN mkdir -p $marmotta_config_dir
COPY karma_wfs_config.properties $marmotta_config_dir
COPY karma_wfs_mappings.properties $marmotta_config_dir
COPY karma_wfs_uris.properties $marmotta_config_dir
RUN mkdir -p $marmotta_dir/WEB-INF/lib
COPY $jar/ldclient-provider-karma-wfs-3.3.0.jar $marmotta_dir/WEB-INF/lib
#COPY karma_wfs_uris.properties $marmotta_dir/system-config.properties

# TODO: Write intialization script to start catalina and move configs
COPY docker-entrypoint.sh /usr/local/bin
ENTRYPOINT ["docker-entrypoint.sh"]

# Tomcat listens on port 8080
EXPOSE 8080
EXPOSE 22

CMD ["catalina.sh", "run"]