from http.server import BaseHTTPRequestHandler
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime
import json
import random
import uuid
import time
from flask import Flask, Response, request
app = Flask(__name__)



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    id = request.args.get('id')
    x = request.args.get('x')
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (id), mimetype="text/html")
