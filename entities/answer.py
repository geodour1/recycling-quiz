class Answer():
    def __init__(self, text="", correct=False, points=0):
        self.text = text
        self.correct = correct
        self.points = points
    
    def to_json(self):
        json_format = {
            "text": self.text,
            "correct": self.correct,
            "points": self.points,
        }
        return json_format

    def __repr__(self):
        return f"Answer: {self.text}_{self.points}_{self.correct}"