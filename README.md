auto check in script

#Prepare the Enviroment:

======    Windows   System   =======

1, install python2.7.x, then add the installation dir(such as C:\Program Files (x86)\Python2.7.13) to Path environment(or use the command listed below in cmd)

cmd commands:

set        #see the environment

set Path   #see the environment of Path

set Path=%Path%;C:\Program Files (x86)\Python2.7.13    #append a new dir to Path

2, download and install chromedriver from https://chromedriver.storage.googleapis.com/, we uncompress the executable to python's same dir(C:\Program Files (x86)\Python2.7.13).

then we can run the python scritp now.

======    Linux   System   =======

pip install selenium

wget http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip

wget http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux32.zip

unzip chromedriver_linux64.zip

sudo mv chromedriver /usr/bin/

sudo chmod +x /usr/bin/chromedriver

