from numpy import *

from util import *
from message import *
from agent import *
from config import *


class MessageBoard:

    def __init__(self):

        self.time_step = 0

        self.msgs = []
        self.agents = []

        self.initialize_agents()

    def initialize_agents(self):
        for i in range(agent_count):
            # self.agents[i].append = Agent(i, generate_boolean_function())
            self.agents.append(Agent(i, generate_msg_properties()))

    def get_msg(self, index):
        return self.msgs[index]

    def get_agent(self, index):
        return self.agents[index]

    def next(self):
        self.time_step += 1

        self.generate_messages()

        self.scoring()

    def generate_messages(self):
        for agent in self.agents:
            value = randint(0, 99)
            if agent.is_posting(value):
                self.msgs.append(Message(agent.get_match()))

    def scoring(self):
        if self.msg_count() <= 0:
            return

        match_message_list = [[] for _ in range(self.msg_count())]

        total_score = 0

        for agent in self.agents:
            j = self.generate_message_location()

            message = self.msgs[j]

            if agent.is_match(message.get_msg()):
                match_message_list[j].append(agent)
                total_score += 1

        for agent in self.agents:
            j = 0
            for match in match_message_list:
                message_score = 0
                if match:
                    new_score = len(match) ** 2 / float(total_score ** 2)
                    for match_agent in match:

                        if agent.get_agent_id() == match_agent.get_agent_id():
                            message_score += agent.get_score()

                    rewards = (message_score * new_score) / 2
                    agent.add_score(rewards)
                    self.msgs[j].add_score(rewards)

                j += 1

    def generate_message_location(self):
        if self.msg_count() == 0:
            return 0

        return randint(0, self.msg_count() - 1)

    def msg_count(self):
        return len(self.msgs)

