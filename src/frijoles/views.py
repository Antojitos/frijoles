from flask import jsonify

from frijoles import app, __version__


@app.route("/api/v1/")
def index():
    data = {
        'name': 'frijoles',
        'version': __version__,
        'url': 'http://frijoles.antojitos.io/',
    }
    return jsonify(**data)
