import gunicorn.app.base
from gunicorn.six import iteritems

class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def make_server(port,app):
    options = {
        'bind': '%s:%s' % ('localhost', str(port))
    }
    StandaloneApplication(app, options).run()
