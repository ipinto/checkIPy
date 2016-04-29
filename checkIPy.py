#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import settings
import smtplib
import telegram
import urllib2


def get_arguments():
    parser = argparse.ArgumentParser(description = 'Check your external IP.')
    parser.add_argument('-c', '--console', action='store_true',
                   help = 'print your IP on console (default action)')
    parser.add_argument('-e', '--email', action='store_true',
                   help = 'send an email with your IP')
    parser.add_argument('-t', '--telegram', action='store_true',
                   help = 'send a Telegram message with your IP')
    return parser.parse_args()

def print_ip(ip):
    print ip

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

def send_telegram_message(ip):
    bot = telegram.Bot(token = settings.TELEGRAM_TOKEN)
    bot.sendMessage(chat_id = settings.TELEGRAM_CHAT_ID,
        text = "Your IP is: {}".format(ip))

if __name__ == "__main__":
    ip = urllib2.urlopen(settings.IP_SOURCE).read()
    args = get_arguments()
    if args.email: send_email(ip)
    if args.telegram: send_telegram_message(ip)
    if args.console or (not args.email and not args.telegram): print_ip(ip)
