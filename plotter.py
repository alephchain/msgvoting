import matplotlib.pyplot as plt


def plot(msg_board):
    agents = [x.get_score() for x in msg_board.agents]

    max_score = 0

    for x in msg_board.msgs:
        if x.get_total_score() > max_score:
            max_score = x.get_total_score()

    # max_score = [x.get_total_score() for x in msg_board.msgs if x.get_total_score() > max_score]

    msg_scores = [x.get_total_score() for x in msg_board.msgs]
    msg_contents = [x.get_content() for x in msg_board.msgs]

    scores = [0] * 4

    scores[0] = [x.get_total_score() for x in msg_board.msgs if x.get_content() == "00"]
    scores[1] = [x.get_total_score() for x in msg_board.msgs if x.get_content() == "01"]
    scores[2] = [x.get_total_score() for x in msg_board.msgs if x.get_content() == "10"]
    scores[3] = [x.get_total_score() for x in msg_board.msgs if x.get_content() == "11"]

    summer = [sum(x) for x in scores]

    plt.subplot(221)
    plt.title('Message Returns')
    plt.plot(sorted(msg_scores))
    plt.ylabel("Score")

    plt.subplot(222)
    plt.title('Agent Returns')
    plt.ylabel("Score")
    plt.plot(sorted(agents))

    plt.subplot(223)
    plt.title('Msg Content')
    plt.ylabel("Content 00")
    plt.bar(range(len(summer)), summer)

    # plt.subplot(224)
    # plt.title('Msg Content')
    # plt.ylabel("Content 01")
    # plt.bar(range(len(contents[1])), sorted(contents[1]))

    # plt.subplot(225)
    # plt.title('Msg Content')
    # plt.ylabel("Content 10")
    # plt.bar(range(len(contents[2])), sorted(contents[2]))
    #
    # plt.subplot(226)
    # plt.title('Msg Content')
    # plt.ylabel("Content 11")
    # plt.bar(range(len(contents[3])), sorted(contents[3]))




    plt.show()
