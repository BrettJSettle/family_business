import unittest
import cards


class CardsTest(unittest.TestCase):

  def test_initialization(self):
    card = cards.CONTRACT
    self.assertEqual(card.name, "Contract")
    self.assertEqual(card.type, cards.CardType.ATTACK)

  def test_deck_size(self):
    deck = cards.Deck.build()
    self.assertEqual(len(deck), 56)

  def test_reshuffle(self):
    deck = cards.Deck([cards.CONTRACT])
    self.assertEqual(len(deck), 1)

    # draw the card
    card = deck.draw()
    self.assertEqual(card, cards.CONTRACT)
    self.assertEqual(len(deck), 0)

    # Cannot draw card if deck and discard are empty.
    self.assertRaises(IndexError, deck.draw)

    # Add to discard pile
    deck.discard(card)
    self.assertEqual(len(deck.discard_pile()), 1)

    card2 = deck.draw()
    self.assertEqual(card2, card)
    self.assertEqual(len(deck), 0)
    self.assertEqual(len(deck.discard_pile()), 0)


if __name__ == "__main__":
  unittest.main()
