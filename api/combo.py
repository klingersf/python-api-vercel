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
    idYt = request.args.get('id')
    lang = request.args.get('x')
    transcricao = YouTubeTranscriptApi.get_transcript(idYt, languages=[lang])
    result = json.dumps(
        {
            "id": str(uuid.uuid4()),
            "Data": time.strftime("%m/%d/%Y", time.localtime()) ,
            "videoURL": idYt,
            "idioma": lang,
            "transcription": transcricao
        }, ensure_ascii=False)
    return result
