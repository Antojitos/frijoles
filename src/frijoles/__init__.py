from flask import Flask

__version__ = '0.1.0'

app = Flask(__name__)
app.config.from_object('frijoles.default_settings')
app.config.from_envvar('FRIJOLES_SETTINGS', silent=True)

import frijoles.views
