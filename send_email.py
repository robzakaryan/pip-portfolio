import smtplib
import ssl


def email(message: str):
    host = 'smtp.gmail.com'
    port = 465
    username = 'robzakaryan@gmail.com'
    password = 'uwap higg vjmw ogkp'
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)
