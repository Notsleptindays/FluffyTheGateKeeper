# FluffyTheGateKeeper
TelegramBot for Motion Detection
Software installation
In this section it will be explained what software is needed to use the system and how to install it and configure it in the different devices.
Raspberry Pi
For the system to work we will have to flash a Raspbian  image into an SD card. This task can be done by using a computer with MS Windows, MacOS or a Linux distribution. To illustrate how it is done we will assume that we are using a computer with either Linux distribution or a MacOS installed. 
Once we have downloaded Raspbian image, we will have to follow these steps:
1.	Insert SD card in our computer.
2.	Check what the device name is in the system. To do so we can open a terminal and type the command:
ls /dev | grep mmcblk

3.	Flash the image typing the following command into a terminal:
dd –bs 4M if=<Path to raspbian image> of=<SD card device name>

Note that this is no the only method available to flash an image into an SD card.

Once we have Raspbian installed we have to configure it and install all the required packages needed for the application to work. We will need to install the following packages:
1.	Python, Python Pip and Git. To install them we will have to open a terminal and type:
sudo apt install python python-pip git

2.	Python telegram bot libraries. To install them we will have to open a terminal and type:
pip install python-telegram-bot

3.	Finally, we will have to install the bot. To install it we will have to execute the following command in a terminal:
git clone <URL> && 
cd FluffyTheGateKeeper &&
sudo cp motiondetection_bot /usr/local/bin

Once everything is installed we will have to configure Raspbian to execute the application on each restart, so in case of undesired reboot, because of a power loss or any other reason, the application start running automatically without the need of any human interaction. To accomplish this task, we will have to do the following command:
sudo sed -i 's/exit 0/ motiondetection_bot\nexit 0/g' /etc/rc.local

Arduino
To upload the software into the Arduino device we are going to use Arduino IDE . We download the full software package from the page https://github.com/Notsleptindays/FluffyTheGateKeeper
Once we have done that, we open Arduino IDE application and in the top bar menu click on “File” tab. A dropdown list will be shown, among the displayed items we have to click the one that says “Open”. A file explorer will then show up, we will have to navigate to the location where we downloaded the software and open the file “MotionSensorArduino.ino”.
Finally, we will have to connect the Arduino device through the USB cable to the computer and press the button “upload”. 
  
Mobile devices
In order to operate the software, it is necessary to download Telegram application in our mobile phone. Although this application is multiplatform and can be executed in mobile phones, tablets, computer and web application, it must be paired to a telephone number.
Mobile application is available in all official application stores. We will illustrate how to download the application in an Android device, but similar processes are used to install the application in other platforms.
  
1.	Open Google Play Store application and search the application “Telegram”.
2.	Install Telegram application.
3.	Open Telegram application.
4.	Insert your phone number.
Software operation
Once everything is installed, you will have to start a conversation with the bot in order to operate the system. To do so you will have to search bot’s name in telegram application. The search process has the following steps:
1.	Search for the bot
 
2.	Press start
 
3.	Select command
 

The possible commands for the bot are:
•	/start: a keyboard with the options for the bot will be presented, as well as a brief explanation of the different commands the bot has for possible execution.
•	/help: a brief explanation of the different commands the bot has for possible execution.
•	/alarm: turn the alarm on
•	/home: turn the alarm off.
•	/clear: clears images from System.
•	/image: If the alarm is on, the system will send a picture.
