class Message:
    def __init__(self, code):
        self.content = code
        self.total_score = 0.0
        self.score = 0.0

    def get_msg(self):
        return self.content

    def add_score(self, score):
        self.total_score += self.score
        self.score = score

    def get_score(self):
        return self.score

    def get_total_score(self):
        return self.total_score

    def get_content(self):
        return self.content

