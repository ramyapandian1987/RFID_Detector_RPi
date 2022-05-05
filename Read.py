'''
This RFID detector code reads the data from RFID tags or cards and alerts the user with an email notification.
'''


import time
import RPi.GPIO as GPIO  #GPIO has all functions needed to interact with GPIO pins 
from mfrc522 import SimpleMFRC522 #will enable communication with RFID RC522
import smtplib
from datetime import datetime
from time import sleep


class Emailer:
    def sendmail(self, recipient,  subject, content):
        #Creating the headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " +subject, 
            "To: " + recipient, "MIME-Version 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit

reader = SimpleMFRC522() #creates a copy  of the SimpleMFRC522 as an object, runs its setup function, then stores it in reader variable
print("Place your RFID card or tag near the RFID reader")

while True:
    id,text = reader.read()
    print(id)
    print(text)
    new_id = str(id)
    #print(new_id)
    #send email update
    sleep(20)
    today = datetime.today()
    date = today.strftime("%b-%d-%Y--%H-%M-%S")

    SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
    SMTP_PORT = 587 #Server Port (don't change!)
    GMAIL_USERNAME = '[Enter the sender username]' 
    GMAIL_PASSWORD = '[Enter the password]'

    sender = Emailer()

    sendTo = '[Enter the recipient email id]'
    emailSubject = "IOT Research: RFID recorded on " + date
    emailContent = "This is the RFID Pi in the lab.\n Following ID is recorded in the system -\n" + new_id + "\n Thank you!"
    print(emailContent)

    #Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.
    sender.sendmail(sendTo, emailSubject, emailContent)
    print("Email sent successfully")
    print("Place your RFID card or tag near the RFID reader")
    
