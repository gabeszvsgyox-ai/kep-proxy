from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Letöltjük a képet a VPS-edről
    kep_url = "https://gentox343.duckdns.org/kep.jpg"
    valasz = requests.get(kep_url)
    
    # Visszaküldjük a Discordnak a kép tartalmát, megfelelő fejlécekkel
    resp = Response(valasz.content, mimetype='image/jpeg')
    resp.headers['Content-Length'] = str(len(valasz.content))
    resp.headers['Cache-Control'] = 'no-cache'
    return resp
