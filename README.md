# checkIPy
Script in Python to notify your IP status via terminar or email. Inspired in https://github.com/gexplorer/checkIP

## Configuration
You must edit `settings.py` with your configuration data in order to send emails.

*Gmail configuration file example:*
```python
# SMTP Config
SMTP='smtp.gmail.com:587'
FROM='from_email@gmail.com'
USERNAME='from_email@gmail.com'
PASSWORD='password'

# Send email to
TO='to_email@gmail.com'

# IP endpoint
IP_SOURCE='https://api.ipify.org'
```

## Run script
```bash
$ python checkIPy.py --help
usage: checkIPy.py [-h] [-e]

Check your external IP.

optional arguments:
  -h, --help   show this help message and exit
  -e, --email  send an email with your IP (default: print it on terminal)
```
