from flask import Flask, render_template, request, redirect
import datetime
import os

microwab_app = Flask(__name__,
                     template_folder=os.path.join(os.path.dirname(__file__), 'sample_app/template'),
                     static_folder=os.path.join(os.path.dirname(__file__), 'sample_app/static'))

@microwab_app.route("/")
def main():
    return render_template("index.html", datetime_now=datetime.datetime.now())

@microwab_app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "admin" and password == "password":
            return redirect("/")
        else:
            return render_template("login.html", error="Invalid credentials")
    
    return render_template("login.html")

if __name__ == "__main__":
    microwab_app.run(host="0.0.0.0", port=5050)