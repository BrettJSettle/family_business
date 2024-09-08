"""Card classes and definitions."""

import enum
import random


class CardType(enum.Enum):
  ATTACK = 1
  RESCUE = 2
  COUNTER = 3


class Card:
  """Playable card."""

  def __init__(self, name: str, card_type: CardType, effect: str):
    self._name = name
    self._card_type = card_type
    self._effect = effect  # Description of what the card does

  @property
  def type(self):
    return self._card_type

  @property
  def details(self):
    return self._effect

  @property
  def name(self):
    return self._name

  def __str__(self):
    return self._name


# Cards
CONTRACT = Card(
    "Contract",
    CardType.ATTACK,
    "Place an opponent's mobster on the Hit List.",
)
CONTRACT_NO_MOB_POWER = Card(
    "Contract (no mob power)",
    CardType.ATTACK,
    "Place an opponent's mobster on the Hit List. Unaffected by Mob Power.",
)
CONTRACT_NO_FAMILY_INFLUENCE = Card(
    "Contract (no family influence)",
    CardType.ATTACK,
    "Place an opponent's mobster on the Hit List. Unaffected by Family"
    " Influence.",
)
CONTRACT_IRON_CLAD = Card(
    "Contract (iron clad)",
    CardType.ATTACK,
    "Place an opponent's mobster on the Hit List. Cannot be stopped.",
)
HIT = Card(
    "Hit",
    CardType.ATTACK,
    "Execute any mobster. Place one of yours on the Hit List.",
)
PRIORITY_CONTRACT = Card(
    "Priority Contract",
    CardType.ATTACK,
    "Place an opponent's mobster on the Hit List, and it's placed first"
    " against the wall.",
)
DOUBLE_CONTRACT = Card(
    "Double Contract",
    CardType.ATTACK,
    "Place two of an opponent's mobsters on the Hit List.",
)
VENDETTA = Card(
    "Vendetta",
    CardType.ATTACK,
    "Choose a mobster on the Hit List and eliminate it, and all"
    " mobsters of the same family.",
)
DOUBLE_CROSS = Card(
    "Double Cross",
    CardType.ATTACK,
    "Choose one of your mobsters on the Hit List and eliminate it. Then"
    " choose an opponent's mobster and place it on the Hit List.",
)
TAKE_IT_ON_THE_LAM = Card(
    "Take it on the Lam",
    CardType.RESCUE,
    "Take one of your mobsters off the Hit List and return it to your hand.",
)
PAY_OFF = Card(
    "Pay Off",
    CardType.RESCUE,
    "Take one mobster off the Hit List and return it to its owner.",
)
SUBSTITUTION = Card(
    "Substitution",
    CardType.RESCUE,
    "Replace 1 mobster on the Hit List with any 1 mobster in play.",
)
# Counter Cards
MOB_POWER = Card(
    "Mob Power",
    CardType.COUNTER,
    "Counters CONTRACT, PRIORITY CONTRACT, DOUBLE CONTRACT. Places 1"
    " mobster of the attacking player on the Hit List. In case of"
    " DOUBLE CONTRACT, also put 1 mobster of the targeted player on the"
    " Hit List.",
)
FAMILY_INFLUENCE = Card(
    "Family Influence",
    CardType.COUNTER,
    "Counters CONTRACT, PRIORITY CONTRACT, DOUBLE CONTRACT. When played"
    " against DOUBLE CONTRACT, only the first target is saved; the"
    " second target is still put on the Hit List.",
)
SAFE_HOUSE = (Card("Safe House", CardType.COUNTER, "Counters VENDETTA."),)
FINGER = (Card("Finger", CardType.COUNTER, "Counters TAKE IT ON THE LAM."),)
# Other Attack Cards (No target required)
ST_VALENTIES_DAY_MASSACRE = Card(
    "St. Valentine's Day Massacre",
    CardType.ATTACK,
    "Immediately eliminate all mobsters on the Hit List. This ends a"
    " Mob War, if one is currently in action.",
)
MOB_WAR = Card(
    "Mob War",
    CardType.ATTACK,
    "Immediately starts a Mob War at normal rate, even if there are"
    " less than 6 mobsters on the Hit List.",
)
AMBUSH = Card(
    "Ambush",
    CardType.ATTACK,
    "Immediately starts a Mob War at double rate, even if there are"
    " less than 6 mobsters on the Hit List. At the start of each"
    " player's turn, the first two mobsters on the Hit List are"
    " eliminated.",
)
# Other Rescue Cards (No target required)
POLICE_PROTECTION = Card(
    "Police Protection",
    CardType.RESCUE,
    "Remove any 1 mobster from the Hit List. POLICE PROTECTION cannot"
    " be countered.",
)
INTRIGUE = Card(
    "Intrigue",
    CardType.RESCUE,
    "Rearrange the mobsters on the Hit List. No mobsters may be added"
    " or removed from the Hit List with this.",
)
TRUCE = Card(
    "Truce",
    CardType.RESCUE,
    "This card ends a Mob War. If any of the conditions that trigger a"
    " Mob War persist, immediately start a new Mob War (with single"
    " rate).",
)
FEDERAL_CRACKDOWN = Card(
    "Federal Crackdown",
    CardType.RESCUE,
    "This card returns all mobsters on the Hit List to their players.",
)
TURNCOAT = Card(
    "Turncoat",
    CardType.RESCUE,
    "Swap 1 mobster in the graveyard with any 1 mobster in play. The"
    " mobster going to the graveyard must be from the player with the"
    " most (or tied for most) mobsters in play, and the returned"
    " mobster must go to the player with the least (or tied for least)"
    " mobsters in play.",
)

CARDS = {
    CONTRACT: 12,
    CONTRACT_NO_MOB_POWER: 3,
    CONTRACT_NO_FAMILY_INFLUENCE: 2,
    CONTRACT_IRON_CLAD: 1,
    PRIORITY_CONTRACT: 3,
    DOUBLE_CONTRACT: 3,
    HIT: 1,
    ST_VALENTIES_DAY_MASSACRE: 1,
    DOUBLE_CROSS: 1,
    MOB_WAR: 1,
    AMBUSH: 1,
    VENDETTA: 1,
    TAKE_IT_ON_THE_LAM: 4,
    POLICE_PROTECTION: 2,
    SUBSTITUTION: 2,
    INTRIGUE: 2,
    TRUCE: 1,
    PAY_OFF: 1,
    FEDERAL_CRACKDOWN: 1,
    MOB_POWER: 3,
    FINGER: 2,
    FAMILY_INFLUENCE: 6,
    SAFE_HOUSE: 1,
    TURNCOAT: 1,
}


class Deck:
  """Deck of Family Business cards."""

  def __init__(self, cards: list[Card]):
    self._cards = cards
    self._discard = []

  def draw(self):
    if not self._cards:
      self._cards.extend(self._discard)
      self._discard = []
      random.shuffle(self._cards)
    if not self._cards:
      raise IndexError(
          "No cards in deck or discard pile, this should never happen"
      )
    return self._cards.pop()

  def discard(self, card: Card):
    self._discard.append(card)

  def __len__(self):
    return len(self._cards)

  def discard_pile(self):
    return self._discard

  @staticmethod
  def build():
    cards = []
    for card, count in CARDS.items():
      for _ in range(count):
        cards.append(card)
    random.shuffle(cards)
    return Deck(cards)
