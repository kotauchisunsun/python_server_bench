from tornado_server import make_server
from falcon_app import app

if __name__=="__main__":
    make_server(3000,app)
