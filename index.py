from flask import Flask, render_template
import requests

app = Flask(__name__)


# route == url == link

@app.route("/")
def main():
    rawData = requests.get("http://www.omdbapi.com/?apikey=b917284c&s=batman")
    movies = rawData.json()
    return render_template("home.html", movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
