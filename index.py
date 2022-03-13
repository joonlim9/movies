from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)


@app.route("/")
def main():
    rawData = requests.get("http://www.omdbapi.com/?apikey=b917284c&s=batman")
    movies = rawData.json()
    return render_template("home.html", movies=movies)


@app.route("/single_movie/<title>")
def single_movie(title):
    rawData = requests.get("http://www.omdbapi.com/?apikey=b917284c&t="+title)
    movie = rawData.json()
    return render_template("single_movie.html", movie=movie)


@app.route("/search")
def search_form():
    return render_template("search.html")


@app.route("/search_by_title", methods=["POST"])
def search_by_title():
    title = request.form["title"]
    year = request.form["year"]
    if year != "":
        rawData = requests.get("http://www.omdbapi.com/?apikey=b917284c&s="+title+"&y="+year)
    else:
        rawData = requests.get("http://www.omdbapi.com/?apikey=b917284c&s="+title)
    movies = rawData.json()
    return render_template("search.html", movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
