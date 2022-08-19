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
def contact() -> tuple[dict[str], int]:
    values = request.get_json()

    if (
        len(values["name"]) > 50
        or len(values["email"]) > 100
        or len(values["content"]) > 2000
    ):
        return {"status": 422, "request": "invalid data"}, 422

    send_email(**values)
    return {"status": 200, "request": "OK"}, 200


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html"), 200


@app.errorhandler(404)
def pg404(_):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
