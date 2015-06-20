import requests
import json

from config import conf
from flask import Flask, Response, request, render_template, \
    make_response, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    return Response('ready: 1\nversion: %s\n' % conf['STATUS_VERSION'],
                    content_type='text/plain')

def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5556)
