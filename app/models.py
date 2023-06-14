from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    answers = db.relationship('Answer', backref='student', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    option_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    A1 = db.Column(db.String(64), nullable=True)
    A2 = db.Column(db.String(64), nullable=True)
    A3 = db.Column(db.String(64), nullable=True)
    A4 = db.Column(db.String(64), nullable=True)
    A5 = db.Column(db.String(64), nullable=True)
    A6 = db.Column(db.String(64), nullable=True)
    A7 = db.Column(db.String(64), nullable=True)
    A8 = db.Column(db.String(64), nullable=True)
    A9 = db.Column(db.String(64), nullable=True)
    A10 = db.Column(db.String(64), nullable=True)
    A11 = db.Column(db.String(64), nullable=True)
    A12 = db.Column(db.String(64), nullable=True)
    A13 = db.Column(db.String(64), nullable=True)
    A14 = db.Column(db.String(64), nullable=True)
    A15 = db.Column(db.String(64), nullable=True)
    A16 = db.Column(db.String(64), nullable=True)
    A17 = db.Column(db.String(64), nullable=True)
    A18 = db.Column(db.String(64), nullable=True)
    A19 = db.Column(db.String(64), nullable=True)
    A20 = db.Column(db.String(64), nullable=True)
    A21 = db.Column(db.String(64), nullable=True)
    A22 = db.Column(db.String(64), nullable=True)
    A23 = db.Column(db.String(64), nullable=True)
    A24 = db.Column(db.String(64), nullable=True)
    A25 = db.Column(db.String(64), nullable=True)
    A26 = db.Column(db.String(64), nullable=True)
    A27 = db.Column(db.String(64), nullable=True)

    answer_list = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13,
                   A14, A15, A16, A17, A18, A19, A20, A21, A22, A23, A24, A25,
                   A26, A27]

    def __repr__(self):
        return f'<Answers {", ".join(self.answer_list)}>'
