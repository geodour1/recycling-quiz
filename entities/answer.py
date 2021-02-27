class Answer():
    def __init__(self, text="", points=0):
        self.text = text
        self.points = points

    def to_json(self):
        return self.text

    def __repr__(self):
        return f"Answer: {self.text}_{self.points}"