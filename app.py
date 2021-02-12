from flask import Flask, render_template
from database.setup import create_database

from entities.question import Question
from entities.answer import Answer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test')
def test():
    db = create_database()
    all_questions = []
    for question in db:
        all_questions.append(question.to_json())

    return {"questions": all_questions}


if __name__ == '__main__':
    app.run(debug=True)