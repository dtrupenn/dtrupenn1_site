"""Script executed by Apache via mod_wsgi to create the application.
Environment variables aren't passed via Apache so we fake them here. This gives
us the advantage, however, of being able to make changes to the application
simply by editing this file in place (Apache will automatically re-load the code
if it sees the wsgi file has been edited)."""
import sys
import os

current_dir = os.path.split(os.path.abspath(__file__))[0]
sys.path.insert(0, current_dir)

def application(environ, start_response):
    """Return the WSGI application object"""
    from server import app
    return app(environ, start_response)
