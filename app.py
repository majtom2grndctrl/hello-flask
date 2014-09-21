from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/hello/<name>")
def hello(name):
    return 'Hello %s' %name

if __name__ == "__main__":
    app.run(host=os.environ['IP'],port=int(os.environ['PORT']))