from twisted.web.wsgi import WSGIResource
from twisted.internet import reactor
from twisted.web import server

def make_server(port,app):
    resource = WSGIResource(reactor, reactor.getThreadPool(), app)
    site = server.Site(resource)
    reactor.listenTCP(port, site)
    reactor.run()


