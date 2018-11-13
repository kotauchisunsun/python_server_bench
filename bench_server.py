#coding:utf-8
import sys

def get_app(name):
    if name == "flask":
        from flask_app import app
        return app
    elif name == "falcon":
        from falcon_app import app
        return app

def get_server(name):
    if name == "twisted":
        from twisted_server import make_server
        return make_server
    elif name == "gunicorn":
        from gunicorn_server import make_server
        return make_server
    elif name == "wsgiref":
        from wsgiref_server import make_server
        return make_server
    elif name == "tornado":
        from tornado_server import make_server
        return make_server

if __name__ == "__main__":
    server_type = sys.argv[1]
    app_type = sys.argv[2]
    get_server(server_type)(3000,get_app(app_type))
