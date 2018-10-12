#!/usr/bin/env python
import os
from gevent.pywsgi import WSGIServer
from web import app

def start_prod():
    http_server = WSGIServer(('', 80), app)
    http_server.serve_forever()

def start_dev():
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)

if __name__ == '__main__':
    if 'FLASK_ENV' not in os.environ:
        start_prod()
    elif os.environ['FLASK_ENV'] == 'development':
        start_dev()
    else:
        start_prod()