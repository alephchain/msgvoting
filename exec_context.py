from util import *
from numpy import *
import matplotlib.pyplot as plt
from message_board import *

msg_board = MessageBoard()
for i in range(step_count):
    msg_board.next()
    # print "run: " + str(i)

agents = [x.get_score() for x in msg_board.agents]
msgs = [x.get_score() for x in msg_board.msgs]

plt.plot(sorted(msgs))
# plt.plot(sorted(agents))
# plt.plot(msg_board.match_list)

plt.show()
