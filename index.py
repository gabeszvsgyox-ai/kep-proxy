from flask import Flask, Response, request
import requests

app = Flask(__name__)

@app.route('/image.png')
def kep_proxy():
    kep_url = "https://gentox343.duckdns.org/kep.jpg"
    
    # A Vercel átadja a valódi IP-t a VPS-nek!
    xff = request.headers.get('X-Forwarded-For', request.remote_addr)
    headers = {'X-Forwarded-For': xff}
    
    valasz = requests.get(kep_url, headers=headers)
    
    resp = Response(valasz.content, mimetype='image/jpeg')
    resp.headers['Content-Type'] = 'image/jpeg'
    return resp
