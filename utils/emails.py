# Standard library imports

import smtplib

from email.message import EmailMessage

# Related third party imports

from dotenv import dotenv_values


SECRET = dotenv_values(".env")


def send_email(name: str, email: str, content: str) -> None:
    msg = EmailMessage()

    msg.set_content(content)
    msg["Subject"] = f"{email} | {name}"
    msg["To"] = "amarftw1@gmail.com"

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(SECRET["PORTFOLIO_EMAIL"], SECRET["PORTFOLIO_PASSWORD"])
    server.send_message(msg)
    server.quit()
