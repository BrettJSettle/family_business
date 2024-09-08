"""Module docstring."""

import random
import actions
import cards
import mob
import player


# class MobWarManager:
#   """Manages mob wars in the game."""

#   def __init__(self, game):
#     self.game = game
#     self.is_active = False
#     self.is_double_rate = False

#   def start_mob_war(self, double_rate=False):
#     self.is_active = True
#     self.is_double_rate = double_rate

#   def end_mob_war(self):
#     self.is_active = False
#     self.is_double_rate = False

#   def resolve(self):
#     """Resolve a mob war."""
#     if not self.is_active:
#       return

#     num_eliminations = 2 if self.is_double_rate else 1
#     for _ in range(num_eliminations):
#       if self.game.hit_list:
#         mobster = self.game.hit_list.pop(0)  # Remove from hit list
#         mobster.owner.mob_family.members.remove(mobster)  # Remove from family
#         self.game.graveyard.append(mobster)  # Add to graveyard

#     # Check if mob war should end
#     if not self.game.hit_list or len(self.game.get_mobsters_in_play()) <= 6:
#       self.end_mob_war()


class Game:
  """FamilyBusiness game loop."""

  def __init__(self):
    self._state = "pregame"

    self._families = list(mob.MOB_FAMILIES.values())
    random.shuffle(self._families)

    self._deck = cards.Deck.build()
    self._discard_pile = []
    self._graveyard = []

    self._current_player_index = -1
    self._players = []

    self._hit_list = []
    self._mob_war_rate = 0

  def add_player(self, name: str) -> player.Player:
    if not isinstance(name, str):
      raise ValueError("Player name must be string, not %s" % type(name))
    if any([name == p.name for p in self._players]):
      raise ValueError("Game already has player named %s" % name)
    if not self._families:
      raise ValueError("Game is full.")
    p = player.Player(name)
    p.set_mob(self._families.pop())
    self._players.append(p)
    return p

  def remove_player(self, p: player.Player):
    fam = cards.MOB_FAMILIES[p.family]
    self._families.append(fam)
    self._players.remove(p)

  def available_families(self):
    return [f.name for f in self._families]

  def deal(self):
    if self._state != "playing":
      raise ValueError("Cannot deal until Game.start() is called.")
    print("Dealing to %d players...\n" % len(self._players))
    for p in self._players:
      for _ in range(5):  # Example: deal 5 cards to each
        card = self._deck.draw()
        p.add_card(card)

  def reshuffle_discard(self):
    self._deck.extend(self._discard_pile)
    random.shuffle(self._deck)
    self._discard_pile = []

  def get_state(self):
    state = dict(
        state=self._state,
        players=[p.get_state() for p in self._players],
        deck_size=len(self._deck),
        graveyard_size=len(self._graveyard),
        discard_pile_size=len(self._discard_pile),
    )
    return state

  def start(self):
    """Deal out cards and update config to be in-game."""
    self._state = "playing"
    self.deal()
    self._current_player_index = 0

  def turn(self):
    """Current player takes a turn."""
    current_player = self._players[self._current_player_index]
    print("Current turn: %s" % current_player)

    # 1. Draw cards
    while current_player.num_cards() < 6:
      if not self._deck:
        print("Reshuffling in discard pile...")
        self.reshuffle_discard()
      card = self._deck.draw()
      current_player.add_card(card)

    # 2. Play a card
    played_card = current_player.play_card()
    self._discard_pile.append(played_card)

    # 3. Resolve card effects
    self.handle_card(played_card, current_player)

  def game_loop(self):
    """Game loop with player turns and logic."""
    while True:
      self.turn()

      # 6. Check for win condition
      if self.check_win_condition():
        break

  def counter(self):
    pass
    # Cancels the last action card, or last counter card

  def next_player(self):
    self._current_player_index = (self._current_player_index + 1) % len(
        self._players
    )

  def check_win_condition(self):
    pass

  def add_to_hit_list(self, mobster):
    self._hit_list.append(mobster)

  def choose_target_player(self):
    while True:
      for i, p in enumerate(self._players):
        print("  %d: %s" % (i, p))
      selection = int(input("Choose player: "))
      if selection >= 0 and selection < len(self._players):
        target_player = self._players[selection]
        break
    return target_player

  def choose_target_mobster(self, target_player):
    """Ask player to choose a single mobster from a players hand."""
    while True:
      for i, mobster in enumerate(target_player.members()):
        print("  %d: %s" % (i, mobster))
      selection = int(input("Choose mobster: "))
      if selection >= 0 and selection < len(target_player.members()):
        target_mobster = target_player.members()[selection]
        break
    return target_mobster

  def choose_target_on_hit_list(self, family: str = None):
    while True:
      for i, mobster in enumerate(self._hit_list):
        if family and mobster not in cards.MOBSTER_FAMILIES[family]:
          continue
        print("  %d: %s" % (i, mobster))
      selection = int(input("Choose mobster: "))
      # TODO: fix to limit selection to valid options
      if selection >= 0 and selection < len(self._hit_list):
        target_mobster = self._hit_list[selection]
        break
    return target_mobster

  def handle_card(self, card: cards.Card, actor: player.Player):
    action = actions.Action(actor, card)
    print(action)
    # if card.type == cards.CardType.ATTACK:
    #   self.handle_attack_card(card, actor)
    # elif card.type == cards.CardType.RESCUE:
    #   self.handle_rescue_card(card, actor)
    # elif card.type == cards.CardType.COUNTER:
    #   self.handle_counter_card(card, actor)
    # else:
    #   raise ValueError("Unrecognized card: %s" % card)

  # def handle_attack_card(self, card: cards.Card, actor: player.Player):
  #   """Handle ATTACK type card actions."""
  #   if card == cards.CONTRACT:
  #     target_player = self.choose_target_player()
  #     target_mobster = self.choose_target_mobster(target_player)
  #     self.add_to_hit_list(target_mobster)
  #     # Check for mob war triggers after adding to hit list
  #     self.check_mob_war_triggers()

  #   elif card == cards.PRIORITY_CONTRACT:
  #     target_player = self.choose_target_player()
  #     target_mobster = self.choose_target_mobster(target_player)
  #     self._hit_list.insert(0, target_mobster)  # Place at the beginning
  #     # Check for mob war triggers
  #     self.check_mob_war_triggers()

  #   elif card == cards.DOUBLE_CONTRACT:
  #     target_player = self.choose_target_player()
  #     target_mobster1 = self.choose_target_mobster(target_player)
  #     self.add_to_hit_list(target_mobster1)
  #     if target_player.members():  # If they have another mobster
  #       # Choose from same player
  #       target_mobster2 = self.choose_target_mobster(
  #           target_player=target_player
  #       )
  #       self.add_to_hit_list(target_mobster2)
  #     else:  # Target the same mobster twice
  #       self.add_to_hit_list(target_mobster1)
  #     # Check for mob war triggers
  #     self.check_mob_war_triggers()

  #   elif card == cards.HIT:
  #     target_player = self.choose_target_player()
  #     target_mobster = self.choose_target_mobster(target_player)
  #     target_player.execute(target_mobster)
  #     self._graveyard.append(target_mobster)
  #     if target_mobster in self._hit_list:
  #       self._hit_list.remove(target_mobster)
  #     self.add_to_hit_list(
  #         self.choose_target_mobster(target_player=actor)
  #     )  # Put one of your own on hit list

  #   elif card == cards.ST_VALENTINES_DAY_MASSACRE:
  #     for mobster in self._hit_list:
  #       mobster.owner.mob_family.members.remove(mobster)
  #       self._graveyard.append(mobster)
  #     self._hit_list = []
  #     self.end_mob_war()  # Ends any ongoing mob war

  #   elif card == cards.DOUBLE_CROSS:
  #     # Choose one of your mobsters on hit list.
  #     mobster_to_eliminate = self.choose_target_on_hit_list(actor.family())
  #     actor.execute(mobster_to_eliminate)
  #     self._graveyard.append(mobster_to_eliminate)
  #     self._hit_list.remove(mobster_to_eliminate)
  #     for other_player in self._players:
  #       if other_player != actor:
  #         target_mobster = self.choose_target_mobster(
  #             target_player=other_player
  #         )
  #         self.add_to_hit_list(target_mobster)

  #   elif card == cards.MOB_WAR:
  #     self.start_mob_war()

  #   elif card == cards.AMBUSH:
  #     self.start_mob_war(double_rate=True)

  #   elif card == cards.VENDETTA:
  #     for other_player in self._players:
  #       if other_player != actor:
  #         for _ in range(2):
  #           target_mobster = self.choose_target_mobster(
  #               target_player=other_player
  #           )
  #           self.add_to_hit_list(target_mobster)
  #     self.start_mob_war(double_rate=True)

  # def handle_rescue_card(self, card: cards.Card, actor: player.Player):
  #   """Handle RESCUE type card actions."""
  #   if card == cards.TAKE_IT_ON_THE_LAM:
  #     target_mobster = actor.choose_own_mobster_on_hit_list()
  #     self._hit_list.remove(target_mobster)
  #     actor.hand.append(target_mobster)  # Return to player's hand

  #   elif card == cards.POLICE_PROTECTION:
  #     target_mobster = self.choose_target_on_hit_list()
  #     self._hit_list.remove(target_mobster)
  #     target_mobster.owner.mob_family.members.append(
  #         target_mobster
  #     )  # Return to family

  #   elif card == cards.SUBSTITUTION:
  #     mobster_on_hit_list = self.choose_target_on_hit_list()
  #     target_player = self.choose_target_player()
  #     mobster = self.choose_target_mobster(target_player=target_player)
  #     self._hit_list.remove(mobster_on_hit_list)
  #     mobster_on_hit_list.owner.mob_family.members.append(mobster_on_hit_list)
  #     self._hit_list.append(mobster)
  #     mobster.owner.mob_family.members.remove(mobster)

  #   elif card == cards.INTRIGUE:
  #     # Implement logic for rearranging mobsters on the hit list (player choice)
  #     pass

  #   elif card == cards.TRUCE:
  #     self.end_mob_war()
  #     self.check_mob_war_triggers()  # Check if a new mob war should start

  #   elif card == cards.PAY_OFF:
  #     target_player = self.choose_target_player()
  #     self._hit_list = [
  #         mobster
  #         for mobster in self._hit_list
  #         if mobster.owner != target_player
  #     ]

  #   elif card == cards.FEDERAL_CRACKDOWN:
  #     for mobster in self._hit_list:
  #       mobster.owner.mob_family.members.append(mobster)
  #     self._hit_list = []

  #   elif card == cards.TURNCOAT:
  #     # ... (Implement complex Turncoat logic based on mobster counts)
  #     pass

  # def handle_counter_card(self, card: cards.Card, p: player.Player):
  #   if card == cards.MOB_POWER:
  #     # ... (Implement Mob Power logic based on the attacked card)
  #     pass
  #   elif card == cards.FAMILY_INFLUENCE:
  #     # ... (Implement Family Influence logic)
  #     pass
  #   elif card == cards.FINGER:
  #     # ... (Implement Finger logic)
  #     pass
  #   elif card == cards.SAFE_HOUSE:
  #     # ... (Implement Safe House logic)
  #     pass

  # def check_mob_war_triggers(self):
  #   if len(self._hit_list) >= 6 or len(self.get_mobsters_in_play()) <= 6:
  #     self.start_mob_war()

  #     # ... (implement Hit logic)
  #   # ... handle other attack cards

  def start_mob_war(self, double_rate=False):
    self._mob_war_rate = 2 if double_rate else 1

  def end_mob_war(self):
    self._mob_war_rate = 0

  def get_mobsters_in_play(self):
    mobsters = []
    for p in self._players:
      mobsters.extend(p.members())
    return mobsters


def main() -> None:
  game = Game()
  p1 = game.add_player("Player 1")
  p2 = game.add_player("Player 2")
  p3 = game.add_player("Player 3")

  globals().update({
      "game": game,
      "p1": p1,
      "p2": p2,
      "p3": p3,
  })
  game.start()


if __name__ == "__main__":
  main()
