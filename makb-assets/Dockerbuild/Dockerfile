FROM tomcat:9.0.30-jdk11-openjdk
RUN mkdir /root/.ssh
RUN echo 'StrictHostKeyChecking no' >> /root/.ssh/config
COPY .ssh/* /root/.ssh/
RUN chmod 600 /root/.ssh/*

# Clone asset repo
RUN git clone git@code.chs.usgs.gov:cegis/makb_assets.git /makb_assets

#Remove any keys
RUN for i in `ls /root/.ssh`; do if [ $i != 'config' ]; then rm /root/.ssh/$i; fi; done