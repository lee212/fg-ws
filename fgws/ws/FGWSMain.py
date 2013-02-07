from cherrypy import wsgiserver
from FGWSApps import app
import os

d = wsgiserver.WSGIPathInfoDispatcher({'/': app})
server = wsgiserver.CherryPyWSGIServer((os.environ["FG_HOSTING_IP"], 5000), d)

if __name__ == '__main__':
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
    except:
        server.stop()
