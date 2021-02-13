from flask import Flask, render_template
from database.setup import create_database, create_titles

from logger import Logger

# Initialize database
db = create_database()
titles = create_titles()

# Initialize Logger
logger = Logger()

# Create application
app = Flask(__name__)

### INDEX ROUTE
@app.route('/')
def home():
    return render_template('index.html')


### START QUIZ
# @app.route('/quiz')
# def start_quiz():
#     # Get 10 questions
#     # Pass them to template and render it
#     return render_template('index.html')


### GET RESULTS 
# @app.route('/results/<int:points>')
# def get_results(points):
#     # Get player's title based on results
#     title = "Hmm... I couldn't understand your score... so you should be a Phantom!"
#     for key in titles.keys():
#         if points <= titles[key]['max'] and points >= titles[key]['min']:
#             title = key

#     # Pass them to template and render it
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