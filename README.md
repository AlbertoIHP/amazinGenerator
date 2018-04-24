### INSTALLING THE ENVIRONMENT


1- sudo apt-get install openjdk-8-jre-headless

2- sudo apt-get install openjdk-8-jdk-headless

3- Download node from https://nodejs.org/dist/v9.11.1/node-v9.11.1-linux-x64.tar.xz

4- Uncompress and change the folder name to node and put it inside a new folder in your $HOME/Programas/

5- Download android studio from https://developer.android.com/studio/index.html#linux-bundle

6- Uncompress and change the folder name to androidstudio and put it inside $HOME/Programas/

7- Replace with `sudo subl /etc/environment` with 


NODE_HOME=$HOME/Programas/node

ANDROID_STUDIO_HOME=$HOME/Programas/androidstudio

JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

ANDROID_HOME=$HOME/Android/Sdk

PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:$NODE_HOME/bin:$JAVA_HOME/bin:$ANDROID_STUDIO_HOME/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/tools"


8- load you variables with `source /etc/environment`

9- open android studio by running `studio.sh`

10- Put not import configuration, and then custom

11- Install this:

Android SDK

Android SDK Platform

Android Virtual Device


12- The SDK Manager can be accessed from the "Welcome to Android Studio" screen. Click on "Configure", then select "SDK Manager".

13- install 
Google APIs
Android SDK Platform 23
Intel x86 Atom_64 System Image
Google APIs Intel x86 Atom_64 System Image

14- Create a new virtual machine

15- Done


### CREATING A PROJECT

1- Get inside the amazinGenerator folder.

2- install pip by typing `sudo apt-get install python-pip`

3- with pip install fuzzywuzzy by typing `pip install fuzzywuzzy`

4- Run amazinGenerator by typing `python amazinGenerator.py`

5- Create a project by typing `new project -test`

6- Use project by typing `use project -test`

7- Create 3 components by typing `new component -com1` `new component -com2` `new component -com3`

8- Open android studio and open your virtual machine 

9- Run your project by typing `run project`

10- Press `a` this will deploy the app into expo in your virtual device, also by installing expo in your phone you will deploy it by taking the QR code

11- Enjoy, soon we will have more features, this is just the beggining :D!
