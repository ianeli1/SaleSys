from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
	return render_template("index.html",title = "Homepage")

recent_entries = [
["Bananas", "12312", "69"],
["Apples", "123", "23"],
["Pears","241","342"],
["Bananas", "12312", "69"],
["Apples", "123", "23"],
["Pears","241","342"],
["Bananas", "12312", "69"],
["Apples", "123", "23"],
["Pears","241","342"],
["Bananas", "12312", "69"],
["Apples", "123", "23"],
["Pears","241","342"],
["Bananas", "12312", "69"],
["Apples", "123", "23"],
["Pears","241","342"],
["Bananas", "12312", "69"],
["Apples", "123", "23"],
["Pears","241","342"],
["Bananas", "12312", "69"],
["Apples", "123", "23"],
["Pears","241","342"]
]


@app.route("/inv")
def inventory():
	return render_template("inv.html", recent = recent_entries)

@app.route("/register", methods=["POST"])
def register():
	name = request.form.get("name")
	email = request.form.get("email")
	dorm = request.form.get("dorm")
	if not name or not dorm or not email:
		return render_template("failure.html")
	reg.append(name + " from " + dorm)
	message = "You are now registered!"
	return redirect("/registrants")

@app.route("/zuck")
def zuck():
	return render_template("zuck.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.errorhandler(404)
def page_not_found(e):
	return render_template("error.html",error_code="404")

@app.errorhandler(500)
def page_oop(e):
	return render_template("error.html", error_code="500")
