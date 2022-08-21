# Standard library imports

import os
import requests

from os.path import join, dirname

# Related third party imports

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

WEBHOOK = str(os.environ.get("WEBHOOK"))


def send_email(name: str, email: str, content: str) -> None:
    """Send a post request to the provided webhook in the .env file."""
    link = f"https://mail.google.com/mail/u/0/?source=mailto&to={email}&fs=1&tf=cm&body=Greetings,+this+is+novusys+(Ammar),&su=Response%20from%20novusys"

    requests.post(
        WEBHOOK,
        json={
            "content": f"@everyone - {link}",
            "embeds": [
                {
                    "description": content,
                    "color": 16777215,
                    "footer": {"text": f"{email} | {name}"},
                }
            ],
            "attachments": [],
        },
    )
