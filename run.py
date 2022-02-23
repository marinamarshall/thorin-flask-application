import os
import json
from flask import Flask, render_template, request


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
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    """
    about member_name function
    """
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
        return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    contact function
    """
    if request.method == "POST":
        print(request.form.get("name"))
        print(request.form["email"])
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    """
    careers function
    """
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # Should never be true in a production application/submitted project
        debug=True)
