FROM makb-assets
COPY doiroot.sh /doiroot.sh
RUN /bin/bash -c "chmod a+x /doiroot.sh; \
    apt-get update && apt-get install git ca-certificates wget automake autoconf libtool bison flex g++ gawk  \ 
    gperf libssl1.0-dev make net-tools -y; \
    git clone git://github.com/openlink/virtuoso-opensource.git /virtuoso-opensource; \
    cd /virtuoso-opensource; \
    git checkout develop/7; \
    ./autogen.sh; \
    ./configure; \
    cat binsrc/conductor/mkvad.sh | sed \"s/cp -f/cp -rf/g\" > binsrc/conductor/mkvad2.sh; \
    mv binsrc/conductor/mkvad2.sh binsrc/conductor/mkvad.sh; \
    make; \
    make install"

    