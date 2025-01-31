from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Модель для вопросов
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    answers = db.relationship('Answer', backref='question', lazy=True)

# Модель для ответов
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
