from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html', title='홈 / flask-practice')


@bp.route('/admin')
def index_for_admin():
    return render_template('index.html', title='홈 / flask-practice', username='admin')


@bp.route('/<username>')
def index_for_user(username):
    return render_template('index.html', title='홈 / flask-practice', username=username)