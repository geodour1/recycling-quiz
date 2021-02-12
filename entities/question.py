class Question():
    def __init__(self, text="", fact="", answers=[]):
        self.text = text
        self.fact = fact
        self.answers = answers
    
    def to_json(self):
        answers_arr = []
        for answer in self.answers:
            answers_arr.append(answer.to_json())

        json_format = {
            "text": self.text,
            "fact": self.fact,
            "answers": answers_arr
        }
        return json_format

    def __repr__(self):
        return f"Question: {self.text}_{self.fact}_{self.answers}"