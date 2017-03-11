# -*- coding: utf-8 -*-

from flask import (
    request,
    session,
    redirect,
    url_for,
    abort,
    render_template,
    flash,
    Blueprint
)

from database import (
    Entries
)

from webargs.flaskparser import (
    FlaskParser,
)

from webargs import fields
from settings import config

from async_tasks import add_log


args_parser = FlaskParser()
article_blueprint = Blueprint('article', __name__)


@article_blueprint.route('/')
def show_entries():
    entries = Entries.get(0, 0)
    return render_template('show_entries.html', entries=entries)


@article_blueprint.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    Entries.add(
        title=request.form['title'],
        text=request.form['text']
    )
    add_log.delay("New entry {0} was successfully posted".\
                  format(request.form['title']))
    flash('New entry was successfully posted')
    return redirect(url_for('article.show_entries'))


@article_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('article.show_entries'))
    return render_template('login.html', error=error)


@article_blueprint.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('article.show_entries'))


@article_blueprint.route('/api/articles', methods=['POST'])
def get_articles():
    params = args_parser.parse({
        'page_no': fields.Field(),
        'page_size': fields.Field()
    })
    page_no = params.get('page_no', 1)
    page_size = params.get('page_size', 1)
    offset = (page_no - 1) * page_size
    limit = page_size
    entries = Entries.get(offset, limit)
    count = Entries.get_num()
    articles = []
    for entrie in entries:
        articles.append(dict(
            title=entrie.title,
            text=entrie.text
        ))
    result = {
        "count": count,
        "page_no": page_no,
        "page_size": page_size,
        "articles": articles
    }
    return render_template('entries.html', result=result)

