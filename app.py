from flask import Flask, render_template
from database.setup import create_database, create_titles

from logger import Logger
from helper import Helper

# Initialize database
db = create_database()
titles = create_titles()

# Initialize logger
logger = Logger()

# Initialize helper
helper = Helper(logger)

# Create application
app = Flask(__name__)

### INDEX ROUTE
@app.route('/')
def home():
    return render_template('index.html')


### START QUIZ
@app.route('/quiz')
def start_quiz():
    # Get 5 random questions
    random_questions = helper.get_random_questions(db, 5)
    if random_questions == []:
        return render_template('index.html')
    
    # Make them json
    json_questions = helper.jsonify_questions(random_questions)

    # Pass them to template and render it
    return render_template('quiz.html', questions=json_questions)


### GET RESULTS 
# @app.route('/results/<int:points>')
# def get_results(points):
#     return title


### HEALTH CHECK ROUTE
@app.route('/health')
def health_route():
    logger.info("Application -- OK")
    return "Application -- OK"


### DEBUG ROUTE
# @app.route('/test')
# def test():
#     all_questions = []
#     for question in db:
#         all_questions.append(question.to_json())

#     return {"questions": all_questions}


if __name__ == '__main__':
    app.run(debug=True)