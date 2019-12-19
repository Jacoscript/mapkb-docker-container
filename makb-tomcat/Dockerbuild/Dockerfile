# Creates an image to run MAKB Tomcat server
# WAR FILES ARE TOO LARGE TO STORE IN GITLAB
# IF PROBLEMS COULD BE RESOLVED WITH GITHUB AND MAVEN ON LOCAL WORKSTATIONS
# THIS SCRIPT COULD BE MODIFIED TO BUILD THEM FROM SOURCE
# !!!! .war files must be added to the Dockerbuild folder !!!!

FROM tomcat:9.0.30-jdk11-openjdk-slim
ENV karma karma-web-0.0.1-SNAPSHOT
ENV webapps /usr/local/tomcat/webapps
# Create a user called tomcat with password s3cret to access manager/html
COPY 'tomcat-users.xml' '/usr/local/tomcat/conf'

# Let all hosts (including local machine) access the manager
RUN mkdir -p '/usr/local/tomcat/conf/Catalina/localhost'
COPY 'manager.xml' '/usr/local/tomcat/conf/Catalina/localhost'

# Deploy requisite war files 
COPY 'geoserver.war' $webapps
COPY 'marmotta.war' $webapps
COPY  $karma.war $webapps 

# Deploy USGS Karma4Marmotta
RUN mkdir $webapps/usgs
COPY 'usgs' $webapps/usgs

# Tomcat listens on port 8080
EXPOSE 8080

