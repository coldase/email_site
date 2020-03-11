from flask import Flask, render_template, redirect, request, flash
from time import sleep
import hashlib
from send_mail import send_email

user_name = "035BFE1ED381083C243CAF55CE5E2387938E8762"
hashed_pass = "D3A3BA018C68B264EC9CF6DA5419AA4F80084EDD"

app = Flask(__name__)


@app.route("/")
def landing():
	return redirect("/login")


@app.route("/login", methods=["GET","POST"])
def login_page():
	if request.method == "POST":
		login_username = request.form["login_username"]
		login_password = request.form["login_password"]
		hashed_username = hashlib.sha1(login_username.encode("utf-8")).hexdigest().upper()
		hashed_password = hashlib.sha1(login_password.encode("utf-8")).hexdigest().upper()
		if hashed_password == hashed_pass and hashed_username == user_name:
			return redirect("/log")
		else:
			return redirect("/login")
	return render_template("login.html")		


@app.route("/email", methods=["GET","POST"])
def email_page():
	if request.method == "POST":
		e_usr = request.form["from_email"]
		e_pwd = request.form["password"]
		e_to = request.form["to_email"]
		e_sub = request.form["title"]
		e_msg = request.form["message"]
		try:
			send_email(e_usr, e_pwd, e_to, e_sub, e_msg)
			print("Email Sent...")
			return redirect("/email")
		except:
			print("Error while sending...")
			return redirect("/email")
	return render_template("email.html")

@app.route("/log")
def logginin():
	return render_template("log.html")


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8000)