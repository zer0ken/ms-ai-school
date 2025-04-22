from flask import Blueprint

bp = Blueprint('board', __name__, url_prefix='/board')


@bp.route('/')
def board():
    return '게시판'


@bp.route('/<int:article_id>')
def article(article_id):
    return f'게시판 > 게시글({article_id})'
