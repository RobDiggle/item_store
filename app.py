from flask import Flask, render_template

app = Flask(__name__)

@app.route("/store")
def store():
        return render_template("home.html")


@app.route("/shopping")
def shopping():
        return render_template("shopping.html")


if __name__ == "__main__":
    app.run(debug=True, port=5007)
