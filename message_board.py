from numpy import *

from util import *
from message import *
from agent import *


class MessageBoard:

    def __init__(self):

        self.time_step = 0

        self.msgs = []
        self.agents = []

        self.post_new_messages()

        for i in range(agent_count):
            # self.agents[i].append = Agent(i, generate_boolean_function())
            self.agents.append(Agent(i, generate_msg_properties()))

    def get_msg(self, index):
        return self.msgs[index]

    def get_agent(self, index):
        return self.agents[index]

    def next(self):
        self.time_step += 1

        self.scoring()

    def scoring(self):
        match_message_list = [[] for _ in range(msg_count)]

        total_score = 0

        for agent in self.agents:
            j = generate_message_location()

            message = self.msgs[j]

            if agent.is_match(message.get_msg()):
                match_message_list[j].append(agent)
                total_score += 1

        for agent in self.agents:
            j = 0
            for match in match_message_list:
                message_score = 0
                if match:
                    for match_agent in match:
                        if agent.get_agent_id() == match_agent.get_agent_id():
                            message_score += agent.get_score()
                            agent.add_score(len(match) ** 2 / float(total_score ** 2))
                        self.msgs[j].add_score(message_score * (len(match) ** 2 / float(total_score ** 2)))
                j += 1

    def post_new_messages(self):
        new_msgs = []
        for i in range(msg_count):
            new_msgs.append(Message(generate_msg_properties()))

        self.msgs = new_msgs

