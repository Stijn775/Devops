from flask import flask
from flask import render_template
import datetime

microwab_app = Flask(__name__)

@microwab_app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    microwab_app.run(host="0.0.0.0", port=5050)