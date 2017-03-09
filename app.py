# -*- coding: utf-8 -*-

from settings import config
from flask import (
    Flask,
)
from article import article_blueprint
from database import db_session
app = Flask(__name__)
app.config.update(config)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

app.register_blueprint(article_blueprint)

if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run()





