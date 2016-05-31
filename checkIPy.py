#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import dbManager
import settings
from settings import logging
import smtplib
import sys
import telegram
import urllib2


def get_device_name():
    if settings.DEVICE_NAME: return '[{}] '.format(settings.DEVICE_NAME)
    return ''

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

def send_email(message):
    message = """\
From: {from_address}
To: {to_address}
Subject: {subject}

{message}
    """.format(from_address = settings.FROM,
                to_address = settings.TO,
                subject = '{}My IP status'.format(get_device_name()),
                message = message)

    # Send email
    server = smtplib.SMTP(settings.SMTP)
    server.starttls()
    server.login(settings.USERNAME, settings.PASSWORD)
    server.sendmail(settings.FROM, settings.TO, message)
    server.quit()

def send_telegram_message(message):
    try:
        bot = telegram.Bot(token = settings.TELEGRAM_TOKEN)
    except telegram.error.InvalidToken:
        logging.error("Invalid Token. Check your Telegram token configuration.")
        return

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
            text = get_device_name() + message)
    except telegram.TelegramError:
        logging.error("An error raised sending the Telegram message. " +
            "Please, send a new message to your bot and try again. " +
            "This way we check if the chat_id is not updated.")


if __name__ == "__main__":
    current_ip = urllib2.urlopen(settings.IP_SOURCE).read()
    message = 'My IP is: {}'.format(current_ip)

    args = get_arguments()
    if args.diff:
        last_ip = dbManager.get_last_ip()
        if last_ip == current_ip: sys.exit()
        message = 'My IP has changed: {} -> {}'.format(last_ip, current_ip)

    dbManager.update_ip(current_ip)
    if args.email: send_email(message)
    if args.telegram: send_telegram_message(message)
    if args.console or (not args.email and not args.telegram): print(current_ip)
