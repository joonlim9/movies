from flask import Flask, render_template

app = Flask(__name__)


# route == url == link

@app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)