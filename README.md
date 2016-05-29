# checkIPy
Python script that sends you an email or a [Telegram](https://telegram.org/) message if your IP address changes.

Inspired in [checkIP](https://github.com/gexplorer/checkIP) project.

*Only tested using Python 2.7.10*

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

### Database configuration
By default, your last IP is stored in the file *data.db*, but you can change the file name or location.
```python
# Database
DB_FILE_NAME='data.db'
```

## Run script
```
$ python checkIPy.py --help
usage: checkIPy.py [-h] [-d] [-c] [-e] [-t]

Check your external IP.

optional arguments:
  -h, --help      show this help message and exit
  -d, --diff      check if the IP changed since last time. If it didn't, it will do nothing.
  -c, --console   print your IP on console (default action)
  -e, --email     send an email with your IP
  -t, --telegram  send a Telegram message with your IP
```

### Examples
* Show my current IP: `$ python checkIPy.py` -> `1.2.3.4`

* Show my current IP and send me an email: `$ python checkIPy.py -ce` -> `1.2.3.4`

* Show my current IP only if it changed since last time: `$ python checkIPy.py --diff` -> `4.3.2.1`

* Show and send my current IP via email and Telegram only if it changed since last time: `$ python checkIPy.py -dcet`
