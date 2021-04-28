FROM makb-tomcat
COPY doiroot.sh /doiroot.sh
#RUN /bin/bash -c "chmod a+x /doiroot.sh; \
RUN apt-get update && apt-get install apache2 git ca-certificates wget automake autoconf libtool bison flex g++ gawk  \ 
    gperf libssl1.0-dev make net-tools python3 -y; \
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
    make; \
    a2enmod ssl proxy proxy_http include; \
    mkdir /opt/ssl; \
    wget http://romulus:81/files/certs/er/2020/star.er.usgs.gov_certPack.zip; \
    7z x star.er.usgs.gov_certPack.zip -o/opt/ssl; \
    rm star.er.usgs.gov_certPack.zip; \
    cat /etc/apache2/sites-enabled/000-default.conf | sed -e 's%DocumentRoot /var/www/html%DocumentRoot /var/www/html\n        ProxyPass "/sparql" "http://localhost:8890/sparql"\n        ProxyPassReverse "/sparql" "http://localhost:8890/sparql"%' > /etc/apache2/sites-enabled/000-default.new; \
    mv /etc/apache2/sites-enabled/000-default.new /etc/apache2/sites-enabled/000-default.conf; \
    cat /etc/apache2/sites-enabled/000-default.conf | sed -e 's%<VirtualHost \*:80>%<VirtualHost _default_:443>\n        SSLEngine On\n        SSLCertificateFile /opt/ssl/star.er.usgs.gov.crt\n        SSLCertificateKeyFile /opt/ssl/star.er.usgs.gov.key\n        SSLCertificateChainFile /opt/ssl/DigiCertCA.crt\n        SSLProtocol -all +TLSv1.1 +TLSv1.2\n%' > /etc/apache2/sites-enabled/000-default.new; \
    mv /etc/apache2/sites-enabled/000-default.new /etc/apache2/sites-enabled/000-default.conf; \
    perl -e 'use warnings; use strict;  my $filename = "/etc/apache2/apache2.conf"; my $found_directive = 0;  my $directive = "<Directory /var/www/>\n";  open(my $fh, "<", $filename) or die $!;  while (!eof($fh)) {     defined(my $line = readline $fh) or die "Readline failed: $!";     if ($line eq $directive) {         $found_directive = 1;     }      if ($found_directive) {         $line =~ s/AllowOverride None/AllowOverride All/;     }      print $line; } close($fh); ' > /etc/apache2/apache2.new; \
    mv /etc/apache2/apache2.new /etc/apache2/apache2.conf


    