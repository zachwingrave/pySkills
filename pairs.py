import json

DEFAULTS = [
    ("strength", "athletics"),
    ("dexterity", "acrobatics"),
    ("dexterity", "sleight of hand"),
    ("dexterity", "stealth"),
    ("intelligence", "arcana"),
    ("intelligence", "history"),
    ("intelligence", "investigation"),
    ("intelligence", "nature"),
    ("intelligence", "religion"),
    ("wisdom", "animal handling"),
    ("wisdom", "insight"),
    ("wisdom", "medicine"),
    ("wisdom", "perception"),
    ("wisdom", "survival"),
    ("charisma", "deception"),
    ("charisma", "intimidation"),
    ("charisma", "performance"),
    ("charisma", "persuasion")
  ]

class Pairs:
  def __init__(self):
    self.pairs = []

  def generate(self, data):
    for ability in data["abilities"]:
      for skill in data["skills"]:
        pair = (ability, skill)

        pair_data = {
          "ability": ability,
          "skill": skill
        }

        if pair in DEFAULTS:
          pair_data["default"] = True
        else:
          pair_data["default"] = False

        if pair_data["default"]:
          print("{:<16}".format("Default pair:"), pair)
        else:
          print("{:<16}".format("New pair:"), pair)
          response = input("Justified? (Y/n): ").strip().lower()

          if response in ["", "y", "yes"]:
            pair_data["justified"] = True
          else:
            pair_data["justified"] = False

          pair_data["reasoning"] = input("Reasoning: ").strip()

        pair = Pair(pair_data)
        self.pairs.append(pair)

  def get_pairs_json(self):
    pairs_json = []
    for pair in self.pairs:
      pairs_json.append(pair.__dict__)
    return pairs_json

  def load(self, file):
    with open(file, "r") as file:
      pairs_list = json.load(file)
    for pair_data in pairs_list["pairs"]:
      self.pairs.append(Pair(pair_data))

  def save(self):
    pairs = self.pairs
    self.pairs = self.get_pairs_json()
    with open("json/pairs.json", "w") as file:
      json.dump(self.__dict__, file, indent =4)
    self.pairs = pairs

class Pair:
  def __init__(self, pair_data):
    self.ability = pair_data["ability"]
    self.skill = pair_data["skill"]
    self.default = pair_data["default"]

    if not self.default:
      self.justified = pair_data["justified"]
      self.reasoning = pair_data["reasoning"]
