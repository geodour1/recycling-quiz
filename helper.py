import random

class Helper():
    def __init__(self, logger):
        self.log = logger

    def calculate_results(self, titles, points):
        # Get player's title based on results
        title = "Hmm... I couldn't understand your score... so you should be a Phantom!"
        for key in titles.keys():
            if points <= titles[key]['max'] and points >= titles[key]['min']:
                title = key
        return title
    
    def get_random_questions(self, questions, number):
        random.shuffle(questions)
        filtered_list = []
        x = range(number)
        index = 0
        for i in x:
            questions[i].index = index
            filtered_list.append(questions[i])
            index += 1

        self.log.info(f"Got {len(filtered_list)} random questions.")
        return filtered_list
    
    def jsonify_questions(self, questions):
        all_questions = []
        for question in questions:
            all_questions.append(question.to_json())
        return all_questions