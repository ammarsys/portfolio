# Standard library imports

import os
import requests

from os.path import join, dirname

# Related third party imports

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

WEBHOOK = os.environ.get("WEBHOOK")


def send_email(name: str, email: str, content: str) -> None:
    """Send a post request to the provided webhook in the .env file."""
    requests.post(
        WEBHOOK,
        json={
            "content": "@everyone - please respond to this email",
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
