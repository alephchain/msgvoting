class Agent:
    def __init__(self, agent_id, boolean_function):
        self.agent_id = agent_id

        self.boolean_function = boolean_function
        self.score = 50.00
        self.post_probability = 0.1

    def is_match(self, msg):
        match = self.boolean_function == msg
        return match
        # return 1 == 1

    def get_score(self):
        return self.score

    def add_score(self, plus_score):
        self.score += plus_score

    def get_agent_id(self):
        return self.agent_id
