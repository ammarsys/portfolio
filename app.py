# Third party / library specific imports

from flask import render_template, Flask


app = Flask(__name__)


@app.route('/')
def index() -> str:
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
