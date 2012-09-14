#!/usr/bin/env python
from optparse import OptionParser

import smtplib
from email.mime.text import MIMEText

sender = 'blazej.autosender@gmail.com'
recipients = 'bwieliczko@gmail.com'

import sys

message = sys.argv[1]

msg = MIMEText(message)
msg['Subject'] =  'automessage'
msg['From'] = sender
msg['To'] = recipients

smtpserver = 'smtp.gmail.com'
smtpuser = 'blazej.autosender'         # set SMTP username here
smtppass = 'zlagluviedle'   # set SMTP password here

session = smtplib.SMTP("smtp.gmail.com", 587)
session.ehlo()
session.starttls()
session.ehlo()

session.login(smtpuser, smtppass)

smtpresult = session.sendmail(sender, [recipients], msg.as_string())

if smtpresult:
    errstr = ""
    for recip in smtpresult.keys():
        errstr = """Could not delivery mail to: %s

Server said: %s
%s

%s""" % (recip, smtpresult[recip][0], smtpresult[recip][1], errstr)
    raise smtplib.SMTPException, errstr

session.close()
