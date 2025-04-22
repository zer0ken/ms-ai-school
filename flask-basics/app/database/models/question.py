from app.database import db


class Question(db.Model):
    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    subject = db.Column(
        db.String(200), 
        nullable=False
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
        backref=db.backref('question_set')
    )
    updated_at = db.Column(
        db.DateTime(), 
        nullable=True
    )

    def __repr__(self):
        return f'<Question {self.subject}>'