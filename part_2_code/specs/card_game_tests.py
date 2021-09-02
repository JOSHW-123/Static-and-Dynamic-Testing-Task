import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Spades",9)
        self.card2 = Card("Clubs",5)
        self.card3 = Card("Hearts", 1)


    def test_check_for_ace(self)
    pass