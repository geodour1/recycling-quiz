class Question():
    def __init__(self, text="", fact="", answers=[], correct=0):
        self.text = text
        self.fact = fact
        self.answers = answers
        self.correct = correct

    def to_json(self):
        answers_arr = []
        for answer in self.answers:
            answers_arr.append(answer.to_json())

        json_format = {
            "q": self.text,
            "correctIndex": self.correct,
            "correctResponse": self.fact,
            "incorrectResponse": self.fact,
            "options": answers_arr
        }
        return json_format

    def __repr__(self):
        return f"Question: {self.text}_{self.fact}_{self.answers}"