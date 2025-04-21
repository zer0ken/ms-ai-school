from flask import Blueprint

bp = Blueprint('board', __name__)


@bp.route('/board')
def board():
    return '게시판'


@bp.route('/board/<int:article_id>')
def article(article_id):
    return f'게시판 > 게시글({article_id})'
