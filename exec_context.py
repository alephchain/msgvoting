from plotter import *
from time import time
from message_board import *


start_time = time()


msg_board = MessageBoard()
for i in range(step_count):
    msg_board.next()
    # print "run: " + str(i)

plot(msg_board)

end_time = time()

print (end_time - start_time)
