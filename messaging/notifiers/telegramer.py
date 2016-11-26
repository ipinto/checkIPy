import settings
import telegram
from settings import logging


class TelegramNotifier:

    def __init__(self, device_name):
        self.device_name = device_name

    def notify(self, message):
        try:
            bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)
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
            bot.sendMessage(chat_id=bot_updates[-1].message.chat_id,
                            text=self.device_name + message)
        except telegram.TelegramError:
            logging.error("An error raised sending the Telegram message. " +
                          "Please, send a new message to your bot and try again. " +
                          "This way we check if the chat_id is not updated.")
