"""Helper class for a player in Family Business."""

import cards
import mob


class Player:
  """Player with mob family and hand of cards."""

  def __init__(self, name: str):
    self._name = name
    self._ready = False
    self._mob_family = None
    self._hand = []  # List to store action cards

  def set_mob(self, mob_family: mob.MobFamily):
    self._mob_family = mob_family

  def get_state(self):
    """Get player info as JSON."""
    state = dict(
        name=self._name,
        ready=self._ready,
    )
    if self._mob_family:
      state["family"] = {
          "name": self._mob_family.name,
          "members": self._mob_family.members,
      }
    return state

  def ready(self, ready):
    self._ready = ready

  @property
  def name(self):
    return self._name

  @property
  def family(self):
    if not self._mob_family:
      return None
    return self._mob_family.name

  def __str__(self):
    return "%s (%s)" % (self._name, self._mob_family.name)

  def execute(self, mobster):
    self._mob_family.members.remove(mobster)
    return mobster

  def hand(self):
    return self._hand.copy()

  def num_cards(self):
    return len(self._hand)

  def add_card(self, card: cards.Card):
    self._hand.append(card)

  def members(self):
    if not self._mob_family:
      return []
    return self._mob_family.members.copy()

  def play_card(self):
    while True:
      for i, card in enumerate(self._hand):
        print("%d: %s" % (i, card))
      n = input("Which card would you like to play: ")
      if n[-1] == "i":
        n = int(n[:-1])
        print(self._hand[n].details())
      else:
        return self._hand.pop(int(n))
