from wsgiref.simple_server import make_server
from pyramid.config import configurator
from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name="hello", renderer="string")
def hello_world(request):
  return "Hello World"
  
 if __name__=="__main__":
      config = configurator()
      config.add_route("hello","hello")
      config.scan()
      app= config.make_wsgi_app()
      server= make_server("0.0.0.0",7070,app)
      server.serve_forever()
