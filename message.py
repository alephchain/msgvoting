class Message:
    def __init__(self, code):
        self.content = code
        self.score = 0

    def get_msg(self):
        return self.content

    def add_score(self, score):
        self.score += score

    def get_score(self):
        return self.score

