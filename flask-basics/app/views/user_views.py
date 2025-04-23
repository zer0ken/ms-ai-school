from flask import Blueprint, url_for, g, render_template
from werkzeug.utils import redirect

from app.db import db
from app.models import User


bp = Blueprint('user', __name__, url_prefix='/user/')


@bp.route('/<username>/')
def profile(username: str) -> str:
    user = User.query.filter_by(username=username).first()
    return render_template('user.html', user=user or None)