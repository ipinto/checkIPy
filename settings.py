import logging

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# SMTP Config
SMTP='smtp.gmail.com:587'
FROM='from_email@gmail.com'
USERNAME='from_email@gmail.com'
PASSWORD='password'

# Send email to
TO='to_email@gmail.com'

# IP endpoint
IP_SOURCE='https://api.ipify.org'

# Telegram Bot
TELEGRAM_TOKEN='your_bot_token'
# chatId = bot.getUpdates()[-1].message.chat_id
TELEGRAM_CHAT_ID='your_chat_id'
