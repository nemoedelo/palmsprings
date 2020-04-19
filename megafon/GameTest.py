import unittest

from megafon.CardGenerator import CardGenerator
from megafon.Game import Game


class MyTestCase(unittest.TestCase):
    def test_game(self):
        card_generator = CardGenerator()
        game = Game(card_generator, "auto")  # or "manual"
        game.start()


if __name__ == '__main__':
    unittest.main()
