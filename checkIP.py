#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
import urllib2
import settings

def send_email():
    message = """\
    From: {from_address}
    To: {to_address}
    Subject: {subject}

    {message}
    """.format(from_address = settings.FROM,
                to_address = settings.TO,
                subject = 'Your IP status',
                message = 'Your IP is: {}'.format(urllib2.urlopen(settings.IP_SOURCE).read()))

    # Send email
    server = smtplib.SMTP(settings.SMTP)
    server.starttls()
    server.login(settings.USERNAME, settings.PASSWORD)
    server.sendmail(settings.FROM, settings.TO, message)
    server.quit()

if __name__ == "__main__":
    send_email()
