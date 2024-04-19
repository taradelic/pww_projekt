from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/osnovno")
def osnovno():
    return render_template("osnovno.html")

@app.route("/phyton")
def phyton():
    return render_template("phyton.html")

@app.route("/flask")
def flask():
    return render_template("flask.html")


if __name__ == "__main__":
    app.run()