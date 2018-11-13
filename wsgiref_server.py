from wsgiref.simple_server import make_server as _make_server
from flask_app import app

def make_server(port,app):
    with _make_server('', port, app) as httpd:
        httpd.serve_forever()

