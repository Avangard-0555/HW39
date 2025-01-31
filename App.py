from flask import Flask, render_template, request, redirect, url_for
from models import db, Question, Answer

app = Flask(__name__)

# Настройки подключения к SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Создание базы данных
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    questions = Question.query.all()
    return render_template('index.html', questions=questions)

@app.route('/question/<int:id>')
def question_detail(id):
    question = Question.query.get_or_404(id)
    return render_template('question.html', question=question)

@app.route('/ask', methods=['GET', 'POST'])
def ask_question():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        new_question = Question(title=title, body=body)
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('ask_question.html')

@app.route('/question/<int:question_id>/answer', methods=['POST'])
def answer_question(question_id):
    body = request.form['body']
    new_answer = Answer(body=body, question_id=question_id)
    db.session.add(new_answer)
    db.session.commit()
    return redirect(url_for('question_detail', id=question_id))

if __name__ == '__main__':
    app.run(debug=True)
