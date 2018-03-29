import random


class AI:
    def __init__(self):
        pass

    def random(self, actions):
        """
        Randomly select an action.
        :param actions: A list of valid actions a player can make.
        :return: A single action.
        """
        return random.choice(actions)
