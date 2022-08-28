from flask import Flask, Blueprint, g, request, render_template
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.exceptions import NotFound

import sqlite3
import json
import re

app = Flask(__name__)
DATABASE = 'darzadata/data/playerdata.db'

@app.route("/")
def index():
    return render_template("swrlly/index.html")

@app.route("/projects")
def about():
    return render_template("swrlly/projects.html")

@app.route("/blog")
def blog():
    return render_template("swrlly/blog.html")

@app.route("/music")
def music():
    return render_template("swrlly/music.html")

@app.route("/robots.txt")
def robots():
    return app.send_static_file("robots.txt")

@app.errorhandler(404)
def page_not_found(e):

    # get subdomain
    subdomain = re.search("//(.+)/", request.base_url).group(1).split(".")[0]

    # go through each blueprint to find the prefix that matches the path
    # can't use request.blueprint since the routing didn't match anything
    for bp_name, bp in app.blueprints.items():
        
        if subdomain == bp_name: 
            # get the 404 handler registered by the blueprint
            handler = app.error_handler_spec.get(bp_name).get(404)[NotFound]
            if handler is not None:
                # if a handler was found, return it's response
                return handler(e)
    
    # return original site 404
    return render_template("swrlly/errors/404.html")

# darzacharts

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

darzacharts = Blueprint(name="darzacharts", import_name=__name__, static_folder="static", subdomain="darzacharts")

@darzacharts.route("/api/playercount")
def dplayercount():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM playersOnline WHERE timeScraped >= 1656410400.0")
    results = cur.fetchall()
    results = json.dumps(results)
    return results

@darzacharts.route("/")
def dindex():
    return render_template("darzacharts/index.html")

@darzacharts.errorhandler(404)
def dpage_not_found(e):
    return render_template("darzacharts/errors/404.html")


app.register_blueprint(darzacharts)
app.config["SERVER_NAME"] = "asfdljkadsjkl.com:8000"
#app.config["SERVER_NAME"] = "swrlly.com"

