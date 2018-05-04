import random


class AI:
    RANDOM = "RANDOM"

    def __init__(self, strategy):
        self.strategy = strategy

    def random(self, actions):
        """
        Randomly select an action.
        :param actions: A list of valid actions a player can make.
        :return: A single action.
        """
        return random.choice(actions)

    def take_action(self, actions):
        if self.strategy == self.RANDOM:
            return self.random(actions)
