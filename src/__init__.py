from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! This is the future home of www.gobulk.co"