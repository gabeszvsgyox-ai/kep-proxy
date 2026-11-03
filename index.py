from flask import Flask, Response
import requests

app = Flask(__name__)

# A te linked a végén az /image.png-vel!
@app.route('/image.png')
def kep_proxy():
    # Letöltjük a képet a te VPS-edről
    kep_url = "https://gentox343.duckdns.org/kep.jpg"
    valasz = requests.get(kep_url)
    
    # Visszaküldjük, mint képfájlt
    resp = Response(valasz.content, mimetype='image/jpeg')
    resp.headers['Content-Type'] = 'image/jpeg'
    resp.headers['Content-Length'] = str(len(valasz.content))
    return resp

# Ha valaki a főoldalra jön, átirányítjuk a képhez
@app.route('/')
def home():
    return '<meta http-equiv="refresh" content="0; url=/image.png">'
