class Agent:
    def __init__(self, agent_id, boolean_function):
        self.agent_id = agent_id

        self.match = boolean_function
        self.score = 50.0
        self.post_probability = 5

    def is_match(self, msg):
        match = self.match == msg
        return match
        # return 1 == 1

    def get_score(self):
        return self.score

    def add_score(self, plus_score):
        self.score += plus_score

    def get_agent_id(self):
        return self.agent_id

    def get_match(self):
        return self.match

    def is_posting(self, value):
        if self.post_probability > value:
            return True

        return False
