from flask_sitemapper import Sitemapper

from typing import List
import time
import re
import os

sitemapper = Sitemapper()
css_version = str(round(time.time()))

def get_site_pages(filename) -> List[List]:
    remove = "app/templates/" + filename

    paths = []
    last_modified = []
    ignore = set(i.strip() for i in open(".gitignore", "r").read().split("\n") if i.strip() != "")
    for subdir, dirs, files in os.walk("app/templates/"):
        
        # ignore unembedded jupyter notebook
        if "jupyter-nb-output" in subdir:
            continue
            
        for file in files:

            if file in ignore or file == "404.html":
                continue

            filepath = subdir + os.sep + file

            if remove in filepath:
                t = time.strftime("%Y-%m-%dT%H:%M%z", time.gmtime(os.path.getmtime(filepath)))
                last_modified.append(t[:-2] + ":" + t[-2:])
                p = re.sub("\\\\", "/", re.sub(remove, "", filepath))
                if p.endswith(".html"): p = p[:-5]
                paths.append(p)

    return paths, last_modified
