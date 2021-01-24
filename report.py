import json

class ReportItem:
  def __init__(self):
    self.new_justified = 0
    self.new_percentage = 0
    self.new_perc_diff = 0

class Ability(ReportItem):
  def __init__(self):
    super().__init__()
    self.defaults = 0
    self.new_skills = 0

class Skill(ReportItem):
  def __init__(self):
    super().__init__()
    self.new_abilities = 0

class Report:
  def __init__(self):
    self.defaults = 0
    self.new_pairs = 0
    self.new_justified = 0

    self.abilities = {}
    self.skills = {}

  def generate(self, data):
    for ability in data["abilities"]:
      self.abilities[ability] = Ability()

    for skill in data["skills"]:
      self.skills[skill] = Skill()

    for pair in data["pairs"]:
      ability = pair.ability
      skill = pair.skill

      if pair.default:
        self.defaults += 1
        self.abilities[ability].defaults += 1
      else:
        self.new_pairs += 1
        self.abilities[ability].new_skills += 1

        if pair.justified:
          self.new_justified += 1
          self.abilities[ability].new_justified += 1

  def get_items_json(self, items):
    items_json = {}
    for item in items.keys():
      items_json[item] = items[item].__dict__
    return items_json

  def save(self):
    self.abilities = self.get_items_json(self.abilities)
    self.skills = self.get_items_json(self.skills)

    with open("json/report.json", "w") as file:
      json.dump(self.__dict__, file, indent=4)
