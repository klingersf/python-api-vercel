from http.server import BaseHTTPRequestHandler
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime
import json
import random
import uuid
import time
from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
