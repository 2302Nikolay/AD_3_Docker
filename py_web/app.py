#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pathlib import Path
from flask import Flask, render_template, request


app = Flask(__name__, template_folder=str(Path(__file__).parent))


@app.route("/home/", methods=['GET','POST'])
def hello_user():
	user = request.args.get('u')
	return render_template("index.html", message = f"Hello, {user}!")


if __name__ == "__main__":
	app.run(host="0.0.0.0")
