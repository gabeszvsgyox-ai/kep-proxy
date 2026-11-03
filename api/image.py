from http.server import BaseHTTPRequestHandler
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Letöltjük a képet a te VPS-edről
        url = "https://gentox343.duckdns.org/kep.jpg"
        response = requests.get(url)
        
        # Visszaküldjük a Discordnak a kép tartalmát
        self.send_response(200)
        self.send_header('Content-Type', 'image/jpeg')
        self.send_header('Content-Length', str(len(response.content)))
        self.end_headers()
        self.wfile.write(response.content)
        return
