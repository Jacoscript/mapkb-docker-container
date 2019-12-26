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
## What this means at a minimum
At a minimum this allows you to do all your development as you've always done.  The Tomcat container is built on Debian Stretch (9.0).  This means Git is installed and APT is available, so if you want to spin up an environment you can install whatever command line tools you prefer (VIM, Emacs, Nano, et al).  Alternatively, if you prefer to write code in Notepad++ and SCP it to the server, you can simply SCP it to the container using the credentials provided above.  What is different, is if you somehow nuke this container, you can revert it back to a known state by calling `docker-compose down` from the repository folder, and then calling `docker-compose up`.  The tomcat install is located at `/usr/local/tomcat` and the webapps folder is located at `/usr/local/tomcat/webapps`.
## A nice workflow using Visual Studio Code
Visual Studio Code has the ability to interact with a remote file system over SSH as if it was working from your local workstation.  We can exploit this to create a very nice workflow for our MAKB containers.
1.  Download [Visual Studio Code.](https://code.visualstudio.com/)
2.  Click on the Extensions Pane and install the Remote - SSH extension provided by Microsoft by clicking the green install button.  If the extension cannot be found simply type "SSH" into the search box:  
![Extensions](images/vs21.png)  
3.  After installing the install button will change to a gear icon:   ![Gear Icon](images/vs31.png)
4.  Find the green arrows at the bottom left corner of the windows and click them.  
![Green Arrows](images/vs41.png)  
The icon appears as follows: ![Green Arrows](images/vs42.png)  
5.  In the resulting popup dialog select Remote-SSH: Connect to Host..., ignoring any other options.  
![Remote-SSH: Connect to Host...](images/vs51.png)  
6.  Select Add New SSH Host..., ignoring any other options  
![Add New SSH Host...](images/vs61.png)  
7.  Type `ssh root@localhost -p 2222` in the dialog box and press Enter  
![SSH Host](images/vs71.png)  
8.  Select the top config file and press enter.  
![SSH Config](images/vs81.png)  
9.  Upon completion, the following dialog box will show up in the lower right corner of the window:  
![SSH Host Configured](images/vs91.png)  
10. Click the green arrows in the lower left hand corner again. ![Green Arrows](images/vs42.png)  
11. In the resulting popup dialog select Remote-SSH: Connect to Host..., ignoring any other options.  
![Remote-SSH: Connect to Host...](images/vs51.png)  
12. Select localhost and press Enter  
![Remote-SSH: localhost](images/vs121.png)  
13. Visual Studio Code will open a new window and ask you to accept the SHA fingerprint, click Continue.  
![Remote-SSH: Fingerprint](images/vs131.png)  
14. Enter the password, in this case __toor__ and press enter.  
![Remote-SSH: Password](images/vs141.png)  
15. Visual Studio Code is now configured to allow you to do development in your container. You can `cd /usr/local/tomcat/webapps` and clone MAKB directly to the webapps folder on the container.
# I've screwed up my development environment, now what?
If you should find yourself in a situation where you've done something that leaves your containers in an unworkable state (or it's just too timeconsuming to fix), simply issue the command `docker-compose down` followed by the command `docker-compose up` from the root of your cloned repository as indicated by the screenshot below:  
![Repaving container](images/screwup1.png)  
__IF YOU ARE DOING ANY DEVELOPMENT INSIDE YOUR CONTAINER MAKE SURE YOU COMMIT AND PUSH ANY CHANGES YOU WISH TO KEEP BEFORE DOING THIS AS THE CONTENTS OF THE CONTAINER WILL BE REVERTED TO THE DEFAULT STATE__  
Any authenication tokens will also be destroyed as well, such as GitLab.  You will need to remove the public key for localhost from `%HOMEPATH%\.ssh\known_hosts`:  
![Known hosts](images/screwup2.png)  

