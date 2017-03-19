# -*- coding: utf-8 -*-

from flask import (
    request,
    session,
    redirect,
    url_for,
    abort,
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

from utils import (
    to_resp,
    error_resp
)

from schema import EntrySchema

args_parser = FlaskParser()
article_blueprint = Blueprint('article', __name__, url_prefix='/api')


@article_blueprint.route('/')
def show_entries():
    entries = Entries.get(0, 0)
    datas = EntrySchema(many=True).dump(entries).data
    return to_resp(datas)


@article_blueprint.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    params = args_parser.parse({
        'title': fields.Field(),
        'text': fields.Field()
    })
    Entries.add(
        title=params['title'],
        text=params['text']
    )
    return redirect(url_for('article.show_entries'))


@article_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = u"登陆异常"
    params = args_parser.parse({
        'username': fields.Field(),
        'password': fields.Field()
    })
    if params['username'] != config['USERNAME']:
        error = 'Invalid username'
    elif params['password'] != config['PASSWORD']:
        error = 'Invalid password'
    else:
        session['logged_in'] = True
        return redirect(url_for('article.show_entries'))
    return error_resp(error, 200, is_status_code=True)

@article_blueprint.route('/is_login', methods=['GET'])
def is_login():
    is_login = session.get('logged_in', False)
    return to_resp(is_login)

@article_blueprint.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('article.show_entries'))


@article_blueprint.route('/articles', methods=['POST'])
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
    articles = EntrySchema(many=True).dump(entries).data
    result = {
        "count": count,
        "page_no": page_no,
        "page_size": page_size,
        "articles": articles
    }
    return to_resp(result)

