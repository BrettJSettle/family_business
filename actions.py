"""Actions that represent card plays."""

import cards
import player


class Action:
  """Action taken by a player with a given card."""

  def __init__(
      self,
      actor: player.Player,
      played_card: cards.Card,
      targets: list[player.Player],
  ):
    self._played_card = played_card
    self._actor = actor
    self._targets = targets
    self._destination = None
    self._counters = []

  def counter(self, actor: player.Player):
    self._counters.append(actor)
