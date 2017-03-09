# -*- coding: utf-8 -*-

from flask import (
    render_template,
    Flask,
    Markup,
    abort,
    redirect,
    url_for
)

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=Markup("<h1>xxx %s</h1>") % Markup('<blink>hacker</blink>'))


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)


if __name__ == "__main__":
    app.run()

