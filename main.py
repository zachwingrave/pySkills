import os
import json
import pairs
import report

DATA_FILE = "json/data.json"
PAIRS_FILE = "json/pairs.json"
REPORT_FILE = "json/report.json"

def main():
  with open("json/data.json", "r") as file:
    data = json.load(file)

  pairs_list = pairs.Pairs()
  if os.path.isfile(PAIRS_FILE):
    with open(PAIRS_FILE, "r") as file:
      pairs_list.load(PAIRS_FILE)
      pairs_list.save()
  else:
      pairs_list = pairs.Pairs()
      pairs_list.generate(data)
      pairs_list.save()

  data["pairs"] = pairs_list.pairs

  report_json = report.Report()
  report_json.generate(data)
  report_json.save()

if __name__ == "__main__":
  main()
