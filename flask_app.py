from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello F2!"

if __name__=="__main__":
    import tornado.wsgi
    container = tornado.wsgi.WSGIContainer(app)
    http_server = tornado.httpserver.HTTPServer(container)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
