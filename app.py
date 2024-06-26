from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/greet", methods=["POST"])
def greet():
    name = request.form["name_input"]
    if name:
        flash(f"Welcome, {name}! Your journey in the mystical land begins now.")
    else:
        flash("Please enter your name to begin the adventure.")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
