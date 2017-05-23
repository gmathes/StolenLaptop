#!/usr/bin/python

import urllib2
import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email import Encoders
import os

gmail_user = "username@gmail.com"                   #gmail account
gmail_pwd = "password"                              #accounts password (yeah i know)
rec = "username@yahoo.com"                          #wherever you want to send to; could be the same as gmail
img = "/Users/username/Documents/theft/ofndr.jpg"           #where the pic gets saved; has to match to below
web_site = "http://www.yourwebsite.com/stolen"              #some file you put up on public webserver once stolen

#have to customize the os.system call below

def sendMail(to, subject, text, attch):

    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(attch,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"'
                   % os.path.basename(attch))
    msg.attach(part)

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()


def check():
    try:
        Stolen = urllib2.urlopen(web_site).read()
    except (urllib2.HTTPError, urllib2.URLError):
        sys.exit()
    else:
        collect()
    
def collect():
    global PublicIP
    PublicIP = urllib2.urlopen('http://whatismyip.org').read()
    os.system('/Users/username/Documents/theft/isightcapture /Users/username/Documents/theft/ofndr.jpg')



check()
sendMail(rec,"Stolen Laptop Info",PublicIP,img)


