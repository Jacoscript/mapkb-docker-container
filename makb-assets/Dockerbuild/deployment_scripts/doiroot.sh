#!/bin/bash

WGETDEB="wget http://romulus.er.usgs.gov:81/files/DOIRootCA2.crt -N -P /usr/share/ca-certificates/extra/"
WGETRPM="wget http://romulus.er.usgs.gov:81/files/DOIRootCA2.crt -N -P /etc/pki/ca-trust/source/anchors/"

if [ -f /etc/redhat-release ] ; then
	echo "Installing for Cent/RHEL 32"
	yum -y install ca-certificates
	update-ca-trust force-enable
	$WGETRPM
	update-ca-trust extract
elif [ ! -f /etc/redhat-release ] ; then
	echo "Installing for Debian/Ubuntu"
	$WGETDEB
	echo "extra/DOIRootCA2.crt" >>	/etc/ca-certificates.conf
	update-ca-certificates
fi
