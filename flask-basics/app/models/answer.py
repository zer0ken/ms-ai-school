from app.db import db


class Answer(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    question_id = db.Column(
        db.Integer,
        db.ForeignKey('question.id', ondelete='CASCADE'),
        nullable=False
    )
    question = db.relationship(
        'Question', 
        backref=db.backref('answers')
    )
    content = db.Column(
        db.Text(), 
        nullable=False
    )
    created_at = db.Column(
        db.DateTime(), 
        nullable=False
    )
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('user.id', ondelete='CASCADE'), 
        nullable=False
    )
    user = db.relationship(
        'User', 
        backref=db.backref('answers')
    )
    updated_at = db.Column(
        db.DateTime(), 
        nullable=True
    )

    def __repr__(self):
        return f'<Answer {self.content[:20]}>'