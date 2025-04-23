from flask import Blueprint, render_template, request, redirect, url_for, g
from datetime import datetime
from app.db import db
from app.models import Question, User, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=['POST'])
def create(question_id):
    question = Question.query.get_or_404(question_id)
    content = request.form['content']
    
    user = g.user if g.user else User.query.filter_by(username='anonymous').first()
    
    answer = Answer(
        content=content,
        created_at=datetime.now(),
        user=user
    )
    question.answers.append(answer)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question.id))
