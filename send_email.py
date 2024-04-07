import smtplib
import ssl
import os


def email(message: str):
    host = 'smtp.gmail.com'
    port = 465
    username = 'robzakaryan@gmail.com'
    password = os.getenv('PASSWORD_GMAIL_SMTP')
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)
