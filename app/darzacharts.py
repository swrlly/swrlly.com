from flask import Blueprint, render_template, g
from .globals import *

import re
import os
import json
import sqlite3

DATABASE = "darzadata/data/playerdata.db"
darzacharts_blueprint = Blueprint(name = "darzacharts", import_name = __name__, static_folder = "static/darzacharts", static_url_path = "/static/darzacharts", subdomain = "darzacharts")
darzaPaths, darzaLastMod = get_site_pages(darzacharts_blueprint.name)

@darzacharts_blueprint.route("/api/playercount")
def dplayercount():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM playersOnline WHERE timeScraped >= 1656410400.0")
    results = cur.fetchall()
    results = json.dumps(results)
    return results

@sitemapper.include(lastmod = darzaLastMod[0])
@darzacharts_blueprint.route("/")
def dindex():
    return render_template("darzacharts/index.html", cssVersion = css_version)

@darzacharts_blueprint.route("/robots.txt")
def drobots():
    return app.send_static_file("darzacharts/robots.txt")

@darzacharts_blueprint.errorhandler(404)
def dpage_not_found(e):
    print(e)
    return render_template("darzacharts/errors/404.html", cssVersion=  css_version)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@darzacharts_blueprint.teardown_app_request
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()