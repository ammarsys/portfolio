# Related third party imports

from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index() -> tuple[str, int]:
    return render_template("index.html"), 200


if __name__ == "__main__":
    app.run()
