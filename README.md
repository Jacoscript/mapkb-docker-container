# Steps for installing
1.  Create a support ticket with the IT Service Desk to install Docker if it is not already installed on your computer.
2.  Clone this repository.
3.  Copy the jar folder from CEGIS_LOCATION into `./makb-tomcat/Dockerbuild`
4.  Start Docker Desktop if it is not already running.
5.  Open a powershell (or bash if on WSL or Linux) prompt and change directory to the location where you cloned your repository.
6.  Type `docker-compose up` to build the images required to host MAKB.  This will take a long time and you will see several pages of messages looking like this:
![Screenshot of install](images/install61.png)
![Screenshot of install](images/install62.png)
7.  Eventually you will a line of text that says `tomcat_1      | 26-Dec-2019 19:15:37.552 INFO [main] org.apache.catalina.startup.Catalina.start Server startup in [27,679] milliseconds`  The number of milliseconds will vary depending on the speed of your computer. 
![Screenshot of install](images/install63.png) 
8.  Congratulations, the MAKB containers have been built.
9.  In the powershell window press CTRL+C to stop the MAKB containers.
# How to start and stop the MAKB containers
If Docker Desktop isn't running, start it.
Open a powershell terminal, (again bash can be used interchangably here) and change directory to the root of your cloned repository.  
Type `docker-compose start` to start the MAKB containers.  
When you are done for the day, type `docker-compose stop` to shutdown the container.   
__There is another command `docker-compose down`, this will destroy the containers and will not give you an opportunity to confirm, use extreme caution before running this command__
# So what do I do with this?
My original goal was to create a sort of shared folder between the tomcat container and the local workstation (a volume in docker terminology). Unfortunately the firewall rules within the organization prevented me from doing so.  Instead I installed SSH in the tomcat container.  
To access the container via SSH, simply point your preferred SSH client at _localhost_ port _2222_.  
If you are using the Windows (or Linux) SSH client thw command is as follows: `ssh root@localhost -p 2222`  
If you are using PuTTY the PuTTY configuration is as follows:  
![PuTTY configuration](images/putty1.png)  
If you are prompted for a username, the username is __root__ the password to log in is __toor__


