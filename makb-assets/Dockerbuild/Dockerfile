FROM tomcat:9.0.30-jdk11-openjdk
RUN mkdir /root/.ssh
RUN echo 'StrictHostKeyChecking no' >> /root/.ssh/config
COPY .ssh/* /root/.ssh/
RUN chmod 600 /root/.ssh/*
COPY karma /root/karma

# Copy over any deployment scripts
COPY deployment_scripts /deployment_scripts
RUN chmod -R a+x /deployment_scripts
RUN chmod -R a-x /deployment_scripts/readme.txt
RUN for i in `ls /deployment_scripts`; do if [[ -x /deployment_scripts/$i ]]; then /deployment_scripts/$i; fi; done

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