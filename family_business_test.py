"""Simple tests for game."""

import unittest
import cards
import family_business as fb
import mob
import player as p


class TestGameSetup(unittest.TestCase):

  def test_initialization(self):
    game = fb.Game()
    p1 = game.add_player("Player 1")
    p2 = game.add_player("Player 2")
    p3 = game.add_player("Player 3")
    p4 = game.add_player("Player 4")
    p5 = game.add_player("Player 5")
    p6 = game.add_player("Player 6")
    self.assertRaises(ValueError, game.add_player, "Player 7")
    
    # ... (Assert initial game state: current player, decks, hit list, etc.)


# class TestGamePlay(unittest.TestCase):

#   def setUp(self):
#     # Create some sample players, families, and cards for testing
#     self.players = [p.Player("Player 1"), p.Player("Player 2")]
#     self.families = [
#         mob.MobFamily("Corleone", "Red"),
#         mob.MobFamily("Soprano", "Blue"),
#     ]
#     self.cards = [
#         cards.Card(
#             "Contract", "Attack", "Place an opponent's mobster on the Hit List."
#         ),
#         # ... add more cards as needed
#     ]

#   def test_initialization(self):
#     game = fb.Game()
#     game.add_player(self.players[0])
#     game.add_player(self.players[1])
#     # ... (Assert initial game state: current player, decks, hit list, etc.)

#   def test_play_card(self):
#     pass
#     # ... (Test playing different types of cards and their effects)

#   def test_counter_play(self):
#     pass
#     # ... (Test counter card plays and their interactions)

#   def test_mob_war(self):
#     pass
#     # ... (Test mob war triggers and resolution)

#   def test_win_condition(self):
#     pass
#     # ... (Test different scenarios to see if the win condition is correctly detected)

#   def test_contract_card(self):
#     # Set up game state with multiple players and mobsters
#     # Player plays a Contract/Priority Contract card
#     # Assert that the targeted mobster is added to the hit list
#     # If Priority Contract, assert it's at the beginning of the list
#     # Assert potential Mob War triggers are checked
#     pass

#   def test_double_contract_card(self):
#     # Set up game state
#     # Player plays a Double Contract card
#     # Assert both targeted mobsters (or the same one twice if only one left) are added to the hit list
#     # Assert potential Mob War triggers are checked
#     pass

#   def test_hit_card(self):
#     # Set up game state
#     # Player plays a Hit card
#     # Assert the targeted mobster is eliminated (removed from family and game)
#     # If the mobster was on the hit list, assert it's removed from there
#     # Assert one of the player's own mobsters is added to the hit list
#     pass

#   def test_st_valentines_day_massacre_card(self):
#     # Set up game state with mobsters on the hit list
#     # Player plays St. Valentine's Day Massacre
#     # Assert all mobsters on the hit list are eliminated
#     # Assert the hit list is empty
#     # If a Mob War was active, assert it's ended
#     pass

#   def test_double_cross_card(self):
#     # Set up game state with player having a mobster on the hit list
#     # Player plays Double Cross
#     # Assert the chosen own mobster is eliminated
#     # Assert one mobster from each opponent is added to the hit list
#     pass

#   def test_mob_war_card(self):
#     # Set up game state
#     # Player plays Mob War/Ambush
#     # Assert a Mob War is started
#     # If Ambush, assert it's double rate
#     pass

#   def test_vendetta_card(self):
#     # Set up game state
#     # Player plays Vendetta
#     # Assert 2 mobsters from each opponent are added to the hit list
#     # Assert a double rate Mob War is started
#     pass

#   def test_take_it_on_the_lam_police_protection_card(self):
#     # Set up game state with mobsters on the hit list
#     # Player plays Take it on the Lam/Police Protection
#     # Assert the targeted mobster is removed from the hit list
#     # If Take it on the Lam, assert it's returned to the player's hand
#     # If Police Protection, assert it's returned to its family
#     pass

#   def test_substitution_card(self):
#     # Set up game state with mobsters on the hit list and in play
#     # Player plays Substitution
#     # Assert the chosen mobster on the hit list is replaced with the chosen mobster in play
#     pass

#   def test_intrigue_card(self):
#     # Set up game state with mobsters on the hit list
#     # Player plays Intrigue
#     # Allow player to rearrange the hit list
#     # Assert the hit list contains the same mobsters but potentially in a different order
#     pass

#   def test_truce_card(self):
#     # Set up game state with an active Mob War
#     # Player plays Truce
#     # Assert the Mob War is ended
#     # If conditions for a new Mob War still exist, assert a new one starts (single rate)
#     pass

#   def test_pay_off_card(self):
#     # Set up game state with mobsters from different players on the hit list
#     # Player plays Pay Off
#     # Assert all mobsters of the targeted player are removed from the hit list
#     pass

#   def test_federal_crackdown_card(self):
#     # Set up game state with mobsters on the hit list
#     # Player plays Federal Crackdown
#     # Assert all mobsters are returned to their respective families
#     # Assert the hit list is empty
#     pass

#   def test_turncoat_card(self):
#     # Set up game state with mobsters in the graveyard and in play
#     # Player plays Turncoat
#     # Assert the correct mobster is moved from graveyard to play
#     #   (from player with most to player with least)
#     # Assert the correct mobster is moved from play to graveyard
#     # If the mobster from the graveyard was on the hit list, assert the new mobster takes its place
#     pass

#   def test_mob_power_family_influence_card(self):
#     # Set up game state where an attack card (Contract, etc.) is played
#     # Another player plays Mob Power/Family Influence
#     # Assert the appropriate mobster is added to/removed from the hit list based on the card and attack
#     pass

#   def test_finger_safe_house_card(self):
#     # Set up game state where Take it on the Lam/Vendetta is played
#     # Another player plays Finger/Safe House
#     # Assert the effects of the Take it on the Lam/Vendetta are cancelled/modified appropriately
#     pass


if __name__ == "__main__":
  unittest.main()
