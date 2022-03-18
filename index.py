from flask import Flask, render_template, request, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = "fdfdfdfd"


@app.route("/")
def main():
    return render_template("home.html")


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
    if not movies:
        movies = False
    return render_template("results.html", movies=movies)


@app.route("/favorite_list")
def favorite_list():
    favorite_list = session.get("favorite")
    if favorite_list == None:
        return redirect(url_for("main"))
    
    return render_template("favorite.html", favorite_list=favorite_list)


@app.route("/add_to_favorite/<title>")
def add_to_favorite(title):
    favorite_list = {}
    if "favorite" in session:
        favorite_list = session.get("favorite")
    else:
        session["favorite"] = {}

    favorite_list[title] = title
    session["favorite"] = favorite_list
    return redirect(url_for("favorite_list"))


if __name__ == "__main__":
    app.run(debug=True)
