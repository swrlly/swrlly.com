# swrlly.com

This repository contains the source code for [swrlly.com](https://swrlly.com). The application server is [Flask](https://flask.palletsprojects.com/en/2.2.x/) and is a good example for properly using blueprints with subdomains.

If you wish to use subdomains with Flask, make sure you do two things:

1. Set `app.config["SERVER_NAME"] = yourwebsite.com` for flask to understand how to properly route subdomains.
2. In order for flask to bind to `yourwebsite.com`, edit your hosts file by adding the line ` 127.0.0.1 yourwebsite.com `

### todo
- [ ] Remove bootstrap as a dependency
- [ ] Design blog format from scratch