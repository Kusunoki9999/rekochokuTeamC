from flask import app, Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/playlist")
def playlist():
    return render_template('playlist.html')

@app.route("/search")
def search():
    return render_template('search.html')

if __name__ == "__main__":
    app.run()