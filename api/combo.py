from http.server import BaseHTTPRequestHandler
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime
import json
import random
import uuid
import time


from flask import Flask, Response, request
app = Flask(__name__);

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    id = request.args.get('id')
    x = request.args.get('x')
    transcricao = YouTubeTranscriptApi.get_transcript('A8zyhKRebus', languages=['pt'])
    result = json.dumps(
        {
            "id": str(uuid.uuid4()),
            "Data": time.strftime("%m/%d/%Y", time.localtime()) ,
            "Numbers": random.sample(range(10),3),
            "videoURL": idVideo,
            "idioma": lang,
            "transcription": transcricao
        }, ensure_ascii=False)
    return result
