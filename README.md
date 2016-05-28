# checkIPy
Script in Python to notify your IP status via:
* Terminal.
* Email.
* [Telegram](https://telegram.org/).

Inspired in [checkIP](https://github.com/gexplorer/checkIP) project.

## Installation
If you want to work with virtual environments:

1. Read *Managing Environments* [documentation](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html).
2. Create a virtual environment for this project: `$ mkvirtualenv checkIPy`.
3. Then, when you want to work on this project: `$ workon checkIPy`.
4. To stop using any virtual environment: `$ deactivate`.

You will need to install all the requirements: `$ pip install -r requirements.txt`.

## Configuration
You must edit `settings.py` file with your configuration data in order to send emails or telegram messages.

### Mail
*Gmail configuration example:*
```python
# SMTP Config
SMTP='smtp.gmail.com:587'
FROM='from_email@gmail.com'
USERNAME='from_email@gmail.com'
PASSWORD='password'

# Send email to
TO='to_email@gmail.com'
```

### IP endpoint
By default we use [ipify](https://api.ipify.org), but you can change the source to your preferred one.
```python
# IP endpoint
IP_SOURCE='https://api.ipify.org'
```

### Telegram bot
Check how to [create a Telegram bot](https://core.telegram.org/bots).

You should create your own bot and include in the configuration file your **bot token**:

```python
# Telegram Bot
TELEGRAM_TOKEN='your_bot_token'
```

The app needs to know the chat id, so you must send a message to your bot in order to start working.

## Run script
```
$ python checkIPy.py --help
usage: checkIPy.py [-h] [-c] [-e] [-t]

Check your external IP.

optional arguments:
  -h, --help      show this help message and exit
  -c, --console   print your IP on console (default action)
  -e, --email     send an email with your IP
  -t, --telegram  send a Telegram message with your IP
```
