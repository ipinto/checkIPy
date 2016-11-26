import settings
import smtplib


class EmailNotifier:

    def __init__(self, device_name):
        self.device_name = device_name

    def notify(self, message):
        message = """\
From: {from_address}
To: {to_address}
Subject: {subject}

{message}
        """.format(from_address=settings.FROM,
                   to_address=settings.TO,
                   subject='{}My IP status'.format(self.device_name),
                   message=message)

        # Send email
        server = smtplib.SMTP(settings.SMTP)
        server.starttls()
        server.login(settings.USERNAME, settings.PASSWORD)
        server.sendmail(settings.FROM, settings.TO, message)
        server.quit()
