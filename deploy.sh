#!/bin/bash
DOCKER='docker'
DOCKER_COMPOSE='docker-compose'
DOI=''
REBUILD_MAKB_ASSETS=''
MAKB_BRANCH='master'
function build_makb_assets() {
    
    if [[ "$REBUILD_MAKB_ASSETS" == "y" || "$REBUILD_MAKB_ASSETS" == "Y" ]]
    then 
        echo "Rebuilding makb-assets image"
        $DOCKER build --no-cache -t makb-assets makb-assets/Dockerbuild
    fi
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
    $DOCKER ps -a > /dev/null 2> /dev/null

    if [[ $? == 1 ]]
    then
        DOCKER="sudo -E $DOCKER"
        DOCKER_COMPOSE="sudo -E $DOCKER_COMPOSE"
    fi
}

function check_ssh() {
    if [  ! -e ~/.ssh/id_* ]
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
    docker > /dev/null 2> /dev/null

    if [[ $? == 0 ]]
    then
        echo "Docker has been found"
    else
        echo "Please install Docker before running this script."
        exit 1
    fi
}

function check_docker_compose() {
    docker-compose > /dev/null 2> /dev/null
    if [[ $? == 1 || $? == 126 ]]
    then
        echo "Docker Compose has been found"
    else
        echo "Please install Docker Compose before running this script."
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
        else
            echo "Specify what branch you'd like to deploy or leave blank for 'master'"
            read __branch
            if [[ "$__branch" != "" ]]
            then
                MAKB_BRANCH="$__branch"
            fi
        fi
    fi
}

function copy_ssh() {
    echo "Copying ssh key into containers"
    cp ~/.ssh/id_* makb-assets/Dockerbuild/.ssh/
    cp ~/.ssh/id_* makb-tomcat/Dockerbuild/.ssh/
}

function checked_deployed() {

    $DOCKER ps -a | grep makb-docker-container > /dev/null

    if [[ $? == 0 ]]
    then
        echo "The MAKB project is already deployed." 
        echo "Run '$DOCKER_COMPOSE start' to launch it."
        echo "Run '$DOCKER_COMPOSE stop' to shut it down."
        echo "To redeploy the MAKB project run '$DOCKER_COMPOSE down' before running this script."
        exit 1
    fi
}

function deploy() {
    if [ -z ${MAKB_SRC+x} ]
    then
        $DOCKER_COMPOSE build
    else
        $DOCKER_COMPOSE build --build-arg ENV=dev
    fi

    if [ -z ${MAKB_SRC+x} ]
    then
        BRANCH="$MAKB_BRANCH"
        export BRANCH
        $DOCKER_COMPOSE up
    elif [[ $MAKB_SRC == "ssh" ]]
    then
        $DOCKER_COMPOSE up
    else
        export MAKB_SRC
        $DOCKER_COMPOSE -f docker-compose.volume.yml up
    fi
}



check_docker
check_docker_compose
confirm_docker_superuser
checked_deployed
confirm_doi_deployment
check_makb_assets_rebuild
check_ssh
check_dev_mode
copy_ssh
create_doiroot_script
build_makb_assets
deploy
