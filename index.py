from flask import Flask

app = Flask(__name__)


# route == url == link

@app.route("/")
def main():
    print("new flask app")


if __name__ == "__main__":
    app.run(debug=True)