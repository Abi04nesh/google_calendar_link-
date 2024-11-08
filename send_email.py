
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

def load_template(filename, replacements):
    with open(filename, 'r') as file:
        template = file.read()
    for key, value in replacements.items():
        template = template.replace(f"{{{{ {key} }}}}", value)
    return template

def send_email(to_address, subject, body):
    msg = MIMEMultipart()
    msg['From'] = config.EMAIL_USER
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    with smtplib.SMTP(config.EMAIL_HOST, config.EMAIL_PORT) as server:
        server.starttls()
        server.login(config.EMAIL_USER, config.EMAIL_PASSWORD)
        server.sendmail(config.EMAIL_USER, to_address, msg.as_string())
