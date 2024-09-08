import unittest
import mob
import player


class TestPlayer(unittest.TestCase):

  def test_initialization(self):
    p = player.Player("Player 1")
    self.assertEqual(p.name, "Player 1")
    self.assertIsNone(p.mob_family)
    self.assertEqual(len(p.hand), 0)  # Initially no cards

  def test_assign_family(self):
    p = player.Player("Player 2")
    p.assign_family(mob.MOB_FAMILIES[0])
    self.assertEqual(p.mob_family.name, mob.MOB_FAMILIES[0].name)

  # def test_all(self):
  #   p = player.Player("me")
  #   d = cards.Deck([cards.CONTRACT])
  #   p.draw(d)


if __name__ == "__main__":
  unittest.main()
