# RFID_Detector_RPi
Detecting RFID tags and cards using MFRC522 module with Raspberry Pi 4 

#### Introduction:

This project uses an RFID scanner to read and write data to a given RFID tag. It also sends email updates that a tag has been scanned. This project was implemented with the Raspberry Pi 4.  Below is a list of steps to execute the project.


#### Materials required: 

•	RFID Scanner – RFID RC522

•	RFID card tag (white)

•	RFID key fob tag (blue)

•	Raspberry Pi 4

•	Header Pins 

•	Soldering Kit

•	7 Female to Female Jumper Cables


#### Circuit connection:

•	SDA connects to Pin 24

•	SCK connects to Pin 23

•	MOSI connects to Pin 19

•	MISO connects to Pin 21

•	GND connects to Pin 6

•	RST connects to Pin 22

•	3.3v connects to Pin 1


![image](https://user-images.githubusercontent.com/37421836/167015218-eaffc717-5507-4c56-9052-d75a87c17a6e.png)

#### Steps:

1.	The RFID scanner requires the header pins to be soldered in place for it to work 

a.	Soldering tutorial : https://www.youtube.com/watch?v=wv5Mp1mn_8M

2.	Once the RFID scanner is soldered, connect the RFID scanner to the raspberry Pi with the jumper wires. 

4.	Power on the Raspberry Pi and configure it

a.	Follow this tutorial to set it up for this project: https://www.raspberrypi-spy.co.uk/2018/02/rc522-rfid-tag-read-raspberry-pi/ 

4.	Write data to the RFID tags using the Write.py program

a.	https://github.com/ramyapandian1987/RFID_Detector_RPi/blob/main/Write.py

5.	Read data from those tags using the Read.py program

a.	https://github.com/ramyapandian1987/RFID_Detector_RPi/blob/main/Read.py

b.	Make sure all the files from GitHub repo are in the same folder, or else the program won’t run correctly

c.	To send email updates, enter the email address you want to use and its corresponding password.

