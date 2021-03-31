FROM makb-tomcat
COPY doiroot.sh /doiroot.sh
#RUN /bin/bash -c "chmod a+x /doiroot.sh; \
RUN    apt-get update && apt-get install git ca-certificates wget automake autoconf libtool bison flex g++ gawk  \ 
    gperf libssl1.0-dev make net-tools -y; \
    wget https://download.osgeo.org/proj/proj-4.9.3.tar.gz; \
    tar xzvf proj-4.9.3.tar.gz; \
    wget http://download.osgeo.org/geos/geos-3.5.1.tar.bz2; \
    tar xvf geos-3.5.1.tar.bz2; \
    git clone git://github.com/openlink/virtuoso-opensource.git /virtuoso-opensource; \
    cd /proj-4.9.3; \
    ./configure; make; make install; \
    cd /geos-3.5.1; \
    ./configure; make; make install; \
    cd /virtuoso-opensource; \
    git checkout develop/7; \
    ./autogen.sh; \
    ./configure --enable-proj4=/usr/local/ --enable-geos=/usr/local/; \
    make

    