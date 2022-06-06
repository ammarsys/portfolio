# Related third party imports

from flask import Flask, request
from flask_cors import CORS

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Local application/library specific imports

from utils import send_email


app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address
)
CORS(app)


@app.route('/api/contact', methods=['POST'])
@limiter.limit(limit_value="2/second")
def contact() -> tuple[dict[str], int]:
    values = request.form.to_dict()

    if len(values['name']) > 50 or len(values['email']) > 100 or len(values['content']) > 2000:
        return {'status': 422, 'request': 'invalid data'}, 422

    send_email(**values)
    return {'status': 200, 'request': 'OK'}, 200


if __name__ == '__main__':
    app.run(debug=True)
