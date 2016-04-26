#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import smtplib
import urllib2
import settings

def get_arguments():
    parser = argparse.ArgumentParser(description='Check your external IP.')
    parser.add_argument('-e', '--email', dest='action', action='store_const',
                   const=send_email, default=print_ip,
                   help='send an email with your IP (default: print it on terminal)')
    return parser.parse_args()

def print_ip(ip):
    print "External IP: {}".format(ip)

def send_email(ip):
    message = """\
From: {from_address}
To: {to_address}
Subject: {subject}

{message}
    """.format(from_address = settings.FROM,
                to_address = settings.TO,
                subject = 'Your IP status',
                message = 'Your IP is: {}'.format(ip))

    # Send email
    server = smtplib.SMTP(settings.SMTP)
    server.starttls()
    server.login(settings.USERNAME, settings.PASSWORD)
    server.sendmail(settings.FROM, settings.TO, message)
    server.quit()

if __name__ == "__main__":
    args = get_arguments()
    args.action(urllib2.urlopen(settings.IP_SOURCE).read())
