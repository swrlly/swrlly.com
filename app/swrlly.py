from flask import Flask, Blueprint, g, request, render_template, abort
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.exceptions import NotFound
from .globals import *

import sqlite3
import time
import json
import re
import os

main_blueprint = Blueprint("swrlly", __name__, static_folder = "static/swrlly/", static_url_path = "/static/swrlly/")
paths, last_modified = get_site_pages(main_blueprint.name)

@main_blueprint.route("/sitemap.xml")
def sitemap():
   return sitemapper.generate()

@main_blueprint.route("/")
def index():
    return render_template("swrlly/index.html", cssVersion = css_version)

@main_blueprint.route("/projects")
def about():
    return render_template("swrlly/projects.html", cssVersion = css_version)

@main_blueprint.route("/blog")
def blog():
    return render_template("swrlly/blog.html", cssVersion = css_version)

@main_blueprint.route("/music")
def music():
    return render_template("swrlly/music.html", cssVersion = css_version)

@main_blueprint.route("/teaching")
def teaching():
    return render_template("swrlly/teaching.html", cssVersion = css_version)

@main_blueprint.route("/robots.txt")
def robots():
    return main_blueprint.send_static_file("robots.txt")

@sitemapper.include(url_variables={"path": paths}, lastmod = last_modified)
@main_blueprint.route("/<path:path>")
def catch_all(path):
    # render_template escapes strings
    print(path)
    try:
        #safe = "/templates/swrlly/"
        if path.endswith(".html"): 
            return render_template("swrlly/errors/404.html", cssVersion = css_version)
        lastEdited = time.asctime(time.gmtime(os.path.getmtime("app/templates/swrlly/" + path + ".html")))
        lastEdited = re.split("\\s+", lastEdited)
        lastEdited = lastEdited[1] + " " + lastEdited[2] + ", " + lastEdited[4] 
        return render_template("swrlly/" + path + ".html", cssVersion = css_version, lastEdited = lastEdited)
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(e)
        return render_template("swrlly/errors/404.html", cssVersion = css_version)

@main_blueprint.errorhandler(404)
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
