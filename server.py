import os
from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/css/foundation.min.css', methods=['GET'])
@app.route('/css/normalize.css', methods=['GET'])
@app.route('/css/app.css', methods=['GET'])
@app.route('/css/fc-webicons.css', methods=['GET'])
@app.route('/js/custom.modernizr.js', methods=['GET'])
@app.route('/imgs/profile.png', methods=['GET'])
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()
