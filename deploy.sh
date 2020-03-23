#!/bin/bash
DOCKER=''
DOCKER_COMPOSE=''
DOI=''
REBUILD_MAKB_ASSETS=''
function build_makb_assets() {
    
    $DOCKER build -t makb-assets makb-assets/Dockerbuild
}

function create_doiroot_script() {
    __script="
#!/bin/bash\n

WGETDEB=\"wget http://romulus.er.usgs.gov:81/files/DOIRootCA2.crt -N -P /usr/share/ca-certificates/extra/\"\n
WGETRPM=\"wget http://romulus.er.usgs.gov:81/files/DOIRootCA2.crt -N -P /etc/pki/ca-trust/source/anchors/\"\n

if [ -f /etc/redhat-release ] ; then\n
	echo \"Installing for Cent/RHEL 32\"\n
	yum -y install ca-certificates\n
	update-ca-trust force-enable\n
	\$WGETRPM\n
	update-ca-trust extract\n
elif [ ! -f /etc/redhat-release ] ; then\n
	echo \"Installing for Debian/Ubuntu\"\n
	\$WGETDEB\n
	echo \"extra/DOIRootCA2.crt\" >>	/etc/ca-certificates.conf\n
	update-ca-certificates\n
fi\n
"
    
    if [[ "$DOI" == "y" || $DOI = "Y" ]]
    then
        echo "Building DOI root certificate script"
        echo -e $__script > makb-assets/Dockerbuild/deployment_scripts/doiroot.sh
    fi

}

function confirm_doi_deployment() {
    echo "Are you deploying to a computer located at DOI (y/n)?"
    read DOI
}

function confirm_docker_superuser() {
    echo "Do you require superuser privileges to run docker and docker-compose (y/n)?"
    read __superuser

    if [[ "$__superuser" == "y" || $__superuser = "Y" ]]
    then
        DOCKER='sudo docker'
        DOCKER_COMPOSE='sudo docker-compose'
    else
        DOCKER='docker'
        DOCKER_COMPOSE='docker-compose'
    fi
}

function check_ssh() {
    if [  ! -e ~/.ssh/id_rsa ]
    then
        echo "Please create an SSH key and add it to GitLab before you run this script."
        exit
    else
        echo "SSH key has been found"
    fi 
}

function check_makb_assets_rebuild() {
    $DOCKER images | grep makb-assets > /dev/null
    if [[ $? == 0 ]]
    then
        echo "The makb-assets image already exists, would you like to rebuild it (y/n)?"
        read REBUILD_MAKB_ASSETS
    else
        echo "The makb-assets image does not exist, it will be built."
        REBUILD_MAKB_ASSETS="y"
    fi

}

function check_docker() {
    which docker

    if [[ $? == 0 ]]
    then
        echo "Docker has been found"
    else
        echo "Please install Docker before running this script."
        exit 1
    fi
}

function check_dev_mode() {
    if [ -z ${MAKB_SRC+x} ]
    then 
        echo "Would you like to build this project for dev mode (y/n)?"
        read __devmode
        if [[ "$__devmode" == "y" || $__devmode = "Y" ]]
        then 
            echo "Please enter your local path to the MAKB source code or leave this blank to use SSH tunneling to transfer files"
            read MAKB_SRC
            if [[ "$MAKB_SRC" == "" ]] 
            then 
                MAKB_SRC=ssh
            fi
        fi
    fi
}
check_docker
#confirm_doi_deployment
#create_doiroot_script

#confirm_docker_superuser
#check_makb_assets_rebuild
#check_ssh
check_dev_mode
echo $MAKB_SRC