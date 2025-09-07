from flask import Flask
from .globals import *

def init():

    app = Flask(__name__, subdomain_matching = True)


    #app.config["SERVER_NAME"] = "localhost:8000"
    app.config["SERVER_NAME"] = "swrlly.com"

    with app.app_context():

        from .swrlly import main_blueprint
        from .darzacharts import darzacharts_blueprint

        app.register_blueprint(main_blueprint)
        app.register_blueprint(darzacharts_blueprint)

        sitemapper.init_app(app)

        return app