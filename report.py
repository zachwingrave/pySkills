import json

class ReportItem:
  def __init__(self):
    self.new_total = 0
    self.new_justified = 0
    self.new_justified_total = 0
    self.new_percentage_diff = 0
    self.justified_percentage = 0
    self.justified_percentage_diff = 0

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
      self.abilities[ability].new_total += 1
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

    for ability in self.abilities.values():
      ability.new_justified_total = ability.defaults + ability.new_justified
      ability.new_percentage_diff = self.percentage_diff(ability.new_total, ability.defaults)
      ability.justified_percentage = self.percentage(ability.new_justified, ability.new_skills)
      ability.justified_percentage_diff = self.percentage_diff(ability.new_skills, ability.new_justified)

  def percentage(self, a, b):
    if b == 0:
      return "NaN"
    else:
      return round((a/b)*100, 2)

  def percentage_diff(self, a, b):
    if b == 0:
      return "NaN"
    else:
      return round(self.percentage(a, b)-100, 2)

  def get_items_json(self, items):
    items_json = {}
    for item in items.keys():
      items_json[item] = items[item].__dict__
    return items_json

  def print_abilities_report(self):
    print("All Ability Scores (Unordered)")
    print("================================\n")
    for ability in self.abilities:
      print("    {}".format(ability.upper()))
      print(json.dumps(self.abilities[ability], indent=4, sort_keys=True))
    input("\nPress [ENTER] to continue.")

  def save(self):
    self.abilities = self.get_items_json(self.abilities)
    self.skills = self.get_items_json(self.skills)

    with open("json/report.json", "w") as file:
      json.dump(self.__dict__, file, indent=4, sort_keys=True)
