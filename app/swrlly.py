from flask import Flask, Blueprint, g, request, render_template, stream_template, abort
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.exceptions import NotFound
from pathlib import Path
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

@main_blueprint.route("/index")
def index_404():
    return page_not_found()

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

@main_blueprint.route("/projects/comprehensive-time-series-analysis")
def time_series_project():
    return stream_template("swrlly/projects/comprehensive-time-series-analysis.html", cssVersion = css_version)

@main_blueprint.route("/robots.txt")
def robots():
    return main_blueprint.send_static_file("robots.txt")

@sitemapper.include(url_variables={"path": paths}, lastmod = last_modified)
@main_blueprint.route("/<path:path>")
def catch_all(path):
    # render_template escapes strings
    try:
        # disallow multiple identical pages
        if path.endswith(".html"): 
            return page_not_found()

        base_dir = Path("app/templates/swrlly").resolve()
        requested_file = (base_dir / (path + ".html")).resolve()

        # check if attempted traversal
        if not str(requested_file).startswith(str(base_dir)):
            return page_not_found()
        
        # check if file exists
        if not requested_file.is_file():
            print("oops")
            return page_not_found()

        # only get time for blog posts
        if path.startswith("blog/"):
            lastEdited = time.asctime(time.gmtime(requested_file.stat().st_mtime))
            lastEdited = re.split("\\s+", lastEdited)
            lastEdited = lastEdited[1] + " " + lastEdited[2] + ", " + lastEdited[4] 
            return stream_template("swrlly/" + path + ".html", cssVersion = css_version, lastEdited = lastEdited)
        else:
            return stream_template("swrlly/" + path + ".html", cssVersion = css_version)

    except Exception as e:
        import traceback
        traceback.print_exc()
        return page_not_found()

@main_blueprint.errorhandler(404)
def page_not_found():
    return render_template("swrlly/errors/404.html", cssVersion = css_version), 404