from http.server import BaseHTTPRequestHandler
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime
import json
import random
import uuid
import time

""" The HTTP request handler """
class handler(BaseHTTPRequestHandler):

  def _send_cors_headers(self):
    """ Sets headers required for CORS """
    self.send_header("Access-Control-Allow-Origin", "*")
    self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
    self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")

  def send_dict_response(self, d):
    """ Sends a dictionary (JSON) back to the client """
    self.wfile.write(bytes(dumps(d), "utf8"))

  def do_OPTIONS(self):
      self.send_response(200)
      self._send_cors_headers()
      self.end_headers()

  def do_GET(self):
    idVideo = request.GET["id"]
    lang = pt
    transcricao = YouTubeTranscriptApi.get_transcript('A8zyhKRebus', languages=['pt'])
    result = json.dumps(
        {
            "id": str(uuid.uuid4()),
            "Data": time.strftime("%m/%d/%Y", time.localtime()) ,
            "Numbers": random.sample(range(10),3),
            "videoURL": idVideo,
            "idioma": lang,
            "transcrição": transcricao
        }, ensure_ascii=False)
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(result.encode(encoding='utf_8'))
    return
