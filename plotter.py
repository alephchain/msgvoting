import matplotlib.pyplot as plt


def plot(msg_board):
    agents = [x.get_score() for x in msg_board.agents]
    msgs = [x.get_total_score() for x in msg_board.msgs]

    plt.subplot(211)
    plt.title('Message Returns')
    plt.plot(sorted(msgs))
    plt.ylabel("Score")
    plt.xlabel("Messages")

    plt.subplot(212)
    plt.title('Agent Returns')
    plt.ylabel("Score")
    plt.xlabel("Agents")
    plt.plot(sorted(agents))

    plt.show()
