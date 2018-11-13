import falcon

class SampleApp:
    def on_get(self, req, resp):
        resp.body = "Hello F1!"
        resp.status = falcon.HTTP_200

app = falcon.API()
app.add_route('/', SampleApp())
