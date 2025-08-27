from flask import Flask, Blueprint, g, request, render_template, abort
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.exceptions import NotFound
from flask_sitemapper import Sitemapper
from pathlib import Path

import sqlite3
import time
import json
import re
import os

app = Flask(__name__)
sitemapper = Sitemapper()
DATABASE = 'darzadata/data/playerdata.db'
lastEdited = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
cssVersion = str(round(time.time()))

baseDir = Path(app.root_path) / "templates/swrlly/"
print("hello", baseDir)

paths = []
darzaPaths = []
for subdir, dirs, files in os.walk("templates/"):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith("404.html"):
            continue

        elif "templates/swrlly" in filepath:
            paths.append(re.sub("templates/swrlly", "", filepath))

        elif "templates/darzacharts" in filepath:
            darzaPaths.append(re.sub("templates/darzacharts", "", filepath))

@app.route("/sitemap.xml")
def sitemap():
  return sitemapper.generate()

@sitemapper.include(lastmod=lastEdited)
@app.route("/")
def Index():
    return render_template("swrlly/index.html", cssVersion=cssVersion)

@sitemapper.include(lastmod=lastEdited)
@app.route("/projects")
def About():
    return render_template("swrlly/projects.html", cssVersion=cssVersion)

@sitemapper.include(lastmod=lastEdited)
@app.route("/blog")
def Blog():
    return render_template("swrlly/blog.html", cssVersion=cssVersion)

@sitemapper.include(lastmod=lastEdited)
@app.route("/music")
def Music():
    return render_template("swrlly/music.html", cssVersion=cssVersion)

@sitemapper.include(lastmod=lastEdited)
@app.route("/robots.txt")
def Robots():
    return app.send_static_file("swrlly/robots.txt")

@sitemapper.include(url_variables={"path": paths}, lastmod=lastEdited)
@app.route("/<path:path>")
def CatchAll(path):
    # render_template escapes strings
    try:
        safe = "/templates/swrlly/"
        #req = (baseDir / path).resolve()
       # print(req)
        #if req.is_relative_to(baseDir):
            #abort(403, "Denied")
            #return
        #print(req.is_relative_to(baseDir))
        #print(os.path.realpath(safe + path + ".html"))
        #print(os.path.commonpath((os.path.realpath(safe + path + ".html"), safe)))
        lastEdited = time.asctime(time.gmtime(os.path.getmtime("templates/swrlly/" + path + ".html")))#".html"))
        lastEdited = lastEdited.split(" ")
        lastEdited = lastEdited[1] + " " + lastEdited[2] + ", " + lastEdited[4] 
        return render_template("swrlly/" + path + ".html", cssVersion=cssVersion, lastEdited = lastEdited)
    except Exception as e:
        print(e, "f")
        return render_template("swrlly/errors/404.html", cssVersion=cssVersion)

@app.errorhandler(404)
def page_not_found(e):

    print("?")

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

@sitemapper.include(lastmod=lastEdited)
@darzacharts.route("/api/playercount")
def dplayercount():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM playersOnline WHERE timeScraped >= 1656410400.0")
    results = cur.fetchall()
    results = json.dumps(results)
    return results

@sitemapper.include(lastmod=lastEdited)
@darzacharts.route("/")
def dindex():
    return render_template("darzacharts/index.html", cssVersion=cssVersion)

@sitemapper.include(lastmod=lastEdited)
@darzacharts.route("/robots.txt")
def drobots():
    return app.send_static_file("darzacharts/robots.txt")

#@sitemapper.include(lastmod=lastEdited)
@darzacharts.errorhandler(404)
def dpage_not_found(e):
    return render_template("darzacharts/errors/404.html", cssVersion=cssVersion)

app.register_blueprint(darzacharts)
sitemapper.init_app(app)

#app.config["SERVER_NAME"] = "swrlly.com"