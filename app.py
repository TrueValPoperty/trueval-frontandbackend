import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port, debug=True)
