#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import sys
import urllib2

import dbManager
import settings
from messaging.messenger import Messenger
from messaging.notifiers.consoler import ConsoleNotifier
from messaging.notifiers.emailer import EmailNotifier
from messaging.notifiers.telegramer import TelegramNotifier


def get_arguments():
    parser = argparse.ArgumentParser(description='Check your external IP.')
    parser.add_argument('-d', '--diff', action='store_true',
                        help='check if the IP changed since last time. ' +
                             "If it didn't, it will do nothing.")
    parser.add_argument('-c', '--console', action='store_true',
                        help='print your IP on console (default action)')
    parser.add_argument('-e', '--email', action='store_true',
                        help='send an email with your IP')
    parser.add_argument('-t', '--telegram', action='store_true',
                        help='send a Telegram message with your IP')
    return parser.parse_args()


def get_device_name():
    if settings.DEVICE_NAME:
        return '[{}] '.format(settings.DEVICE_NAME)
    return ''


def get_message(current_ip, change):
    message = 'My IP is: {}'.format(current_ip)

    if change:
        last_ip = dbManager.get_last_ip()
        if last_ip == current_ip:
            sys.exit()
        message = 'My IP has changed: {} -> {}'.format(last_ip, current_ip)

    return message


def get_ip():
    return urllib2.urlopen(settings.IP_SOURCE).read()


if __name__ == "__main__":
    ip = get_ip()
    messenger = Messenger()
    args = get_arguments()

    if args.email:
        messenger.add_notifier(EmailNotifier(get_device_name()))
    if args.telegram:
        messenger.add_notifier(TelegramNotifier(get_device_name()))
    if args.console or (not args.email and not args.telegram):
        messenger.add_notifier(ConsoleNotifier())

    messenger.notify(get_message(ip, args.diff))

    dbManager.update_ip(ip)
