from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Welcome to Geeks for Geeks</h1>"
