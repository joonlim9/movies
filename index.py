from flask import Flask, render_template

app = Flask(__name__)


# route == url == link

@app.route("/")
def main():
    data = "This is My Movie Search Website"
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)