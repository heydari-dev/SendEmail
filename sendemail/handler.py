from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, body, your_email, your_password, email_receiver):
    msg = MIMEMultipart()
    msg['From'] = your_email
    msg['To'] = email_receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(your_email, your_password)
        server.sendmail(your_email, email_receiver, msg.as_string())

