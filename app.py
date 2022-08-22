# Standard library imports

from typing import Union

# Related third party imports

from flask import Flask, request, render_template
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Local application/library specific imports

from utils import send_email


app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)
CORS(app)


@app.route("/api/contact", methods=["POST"])
@limiter.limit(limit_value="2/second")
def contact() -> tuple[dict[str, Union[int, str]], int]:
    """Contact route, has a ratelimit of 2/second"""
    values = request.get_json()

    if not values:
        return {"status": 400, "request": "bad data or headers"}, 400

    if (
        len(values["name"]) > 50
        or len(values["email"]) > 100
        or len(values["content"]) > 2000
    ):
        return {"status": 422, "request": "invalid data"}, 422

    send_email(**values)
    return {"status": 200, "request": "OK"}, 200


@app.route("/", methods=["GET"])
def index() -> tuple[str, int]:
    return render_template("index.html"), 200


@app.errorhandler(404)  # type: ignore
def pg404(_) -> tuple[str, int]:
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run()
