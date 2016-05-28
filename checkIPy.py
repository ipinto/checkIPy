#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import dbManager
import settings
from settings import logging
import smtplib
import telegram
import urllib2
import sys


def get_arguments():
    parser = argparse.ArgumentParser(description = 'Check your external IP.')
    parser.add_argument('-d', '--diff', action='store_true',
                   help = 'check if the IP changed since last time. ' +
                          "If it didn't, it will do nothing.")
    parser.add_argument('-c', '--console', action='store_true',
                   help = 'print your IP on console (default action)')
    parser.add_argument('-e', '--email', action='store_true',
                   help = 'send an email with your IP')
    parser.add_argument('-t', '--telegram', action='store_true',
                   help = 'send a Telegram message with your IP')
    return parser.parse_args()

def print_ip(ip):
    print ip

def send_email(message):
    message = """\
From: {from_address}
To: {to_address}
Subject: {subject}

{message}
    """.format(from_address = settings.FROM,
                to_address = settings.TO,
                subject = 'Your IP status',
                message = message)

    # Send email
    server = smtplib.SMTP(settings.SMTP)
    server.starttls()
    server.login(settings.USERNAME, settings.PASSWORD)
    server.sendmail(settings.FROM, settings.TO, message)
    server.quit()

def send_telegram_message(message):
    bot = telegram.Bot(token = settings.TELEGRAM_TOKEN)
    try:
        logging.debug(bot.getMe())
    except telegram.error.Unauthorized:
        logging.error("Unauthorized. Check your Telegram credentials.")
        return

    bot_updates = bot.getUpdates()
    if not bot_updates or not bot_updates[-1].message.chat_id:
        logging.error("We need your telegram chat id. Please, send any message to your bot.")
        return

    try:
        sent_message = bot.sendMessage(chat_id = bot_updates[-1].message.chat_id,
            text = message)
    except telegram.TelegramError:
        logging.error("An error raised sending the Telegram message. " +
            "Please, send a new message to your bot and try again. " +
            "This way we check if the chat_id is not updated.")


if __name__ == "__main__":
    current_ip = urllib2.urlopen(settings.IP_SOURCE).read()
    message = 'Your IP is: {}'.format(current_ip)

    args = get_arguments()
    if args.diff:
        last_ip = dbManager.get_last_ip()
        if last_ip == current_ip: sys.exit()
        message = 'Your IP has changed: {} -> {}'.format(last_ip, current_ip)

    dbManager.update_ip(current_ip)
    if args.email: send_email(message)
    if args.telegram: send_telegram_message(message)
    if args.console or (not args.email and not args.telegram): print_ip(current_ip)
