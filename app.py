from flask import Flask, Blueprint, g, request, render_template
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.exceptions import NotFound

import sqlite3
import json
import re
import os

app = Flask(__name__)
DATABASE = 'darzadata/data/playerdata.db'
cssVersion = "17"

@app.route("/")
def Index():
    return render_template("swrlly/index.html", cssVersion=cssVersion)

@app.route("/projects")
def About():
    return render_template("swrlly/projects.html", cssVersion=cssVersion)

@app.route("/blog")
def Blog():
    return render_template("swrlly/blog.html", cssVersion=cssVersion)

@app.route("/music")
def Music():
    return render_template("swrlly/music.html", cssVersion=cssVersion)

@app.route("/robots.txt")
def Robots():
    return app.send_static_file("swrlly/robots.txt")

@app.route("/<path:path>")
def CatchAll(path):
    # render_template escapes strings
    try:
        return render_template("swrlly/" + path + ".html", cssVersion=cssVersion)
    except:
        return render_template("swrlly/errors/404.html")

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

@darzacharts.route("/robots.txt")
def drobots():
    return app.send_static_file("darzacharts/robots.txt")

@darzacharts.errorhandler(404)
def dpage_not_found(e):
    return render_template("darzacharts/errors/404.html")

blog = Blueprint(name="blog", import_name=__name__, static_folder="static", subdomain="blog")

@blog.route("/")
def bindex():
    return "test"


app.register_blueprint(darzacharts)
app.register_blueprint(blog)
app.config["SERVER_NAME"] = "swrlly.com"