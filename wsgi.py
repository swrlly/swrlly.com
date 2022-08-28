from app import *

if __name__ == "__main__":
    #app.config["SERVER_NAME"] = "asfdljkadsjkl.com:8000"
    app.config["SERVER_NAME"] = "swrlly.com"
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )
    app.run(port = 8000)
