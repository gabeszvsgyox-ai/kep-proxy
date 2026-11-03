from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Letöltjük a képet a te VPS-edről
    kep_url = "https://gentox343.duckdns.org/kep.jpg"
    valasz = requests.get(kep_url)
    
    # Visszaküldjük a Discordnak, mint képet
    return Response(valasz.content, mimetype='image/jpeg')

@app.route('/favicon.ico')
def favicon():
    return '', 204
