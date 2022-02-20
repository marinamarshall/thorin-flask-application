import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """
    index function
    """
    return render_template("index.html")


@app.route("/about")
def about():
    """
    about function
    """
    return render_template("about.html")


@app.route("/contact")
def contact():
    """
    contact function
    """
    return render_template("contact.html")    


@app.route("/careers")
def careers():
    """
    careers function
    """
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # Should never be true in a production application/submitted project
        debug=True)
