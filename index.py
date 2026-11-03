from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("https://gentox343.duckdns.org/kep.jpg", code=302)
