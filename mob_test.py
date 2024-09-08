import unittest
import mob


class TestMobFamily(unittest.TestCase):

  def test_initialization(self):
    family = mob.MobFamily("Corleone", "Red")
    self.assertEqual(family.name, "Corleone")
    self.assertEqual(family.color, "Red")
    self.assertEqual(len(family.members), 0)  # Initially no members

  def test_add_member(self):
    family = mob.MobFamily("Soprano", "Blue")
    family.add_member("Tony Soprano")
    self.assertEqual(len(family.members), 1)
    self.assertEqual(family.members[0], "Tony Soprano")


if __name__ == "__main__":
  unittest.main()
