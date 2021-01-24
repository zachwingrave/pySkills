[![Run on Repl.it](https://repl.it/badge/github/zachwingrave/pySkills)](https://repl.it/github/zachwingrave/pySkills)

# pySkills

An investigation into the fairness of mixing ability scores and skill proficiencies in Dungeons & Dragons 5e, inspired by the crew of the D&D podcast [Of Dice & DMs](https://soundcloud.com/ofdiceanddms). Thanks to Ben, Jeremy and Tory for all their hard work!

## What is this?

In Dungeons & Dragons 5e, there are 6 ability scores and 18 skill proficiencies. In the core rules as written, these 18 skill proficiencies are each paired with a single ability score which, together with a proficiency bonus that represents training in that skill, provides a bonus to skill checks and therefore boosts the likelihood that a player character will succeed at the check in question.

An optional rule states that the ability scores can be mixed and matched according to the Dungeon Master's discretion. For instance, rather than making a Charisma (intimidation) check, a player may instead make a Strength (intimidation) check. This report aims to make some observations on what this would mean in terms of new skills and opportunities for player characters, and assist the reader in forming an educated opinion on whether this optional rule is fair.

## Defining the Rules

For consistency in this report, the following definitions apply:

- A single ability score matched with a single skill proficiency is called a `Pair`.
- A `Pair` which appears on the official 5e character sheet is considered `default`.
- A `Pair` is `justified` if it is not `default` and the user has given their approval.
- A `Pair` that is `justified` must have a `reasoning` provided to support itself.

## By the Numbers

Once the user has provided their responses for `justification` and `reasoning` for non-`default` `Pairs`, the program will create a `pairs.json` file and a `report.json` file. `pairs.json` contains all possible combinations of ability score and skill proficiency, including whether or not it is `default`, `justified` and what the `reasoning` provided was.

`report.json` contains the results of rudimentary analysis of the provided `Pairs`. No objective interpretations are made over these numbers, and the implications are left as an exercise for the reader.

### License
This software is licensed under the [GNU General Public License v3](LICENSE.md).

### Attributions
[Of Dice & DMs](https://soundcloud.com/ofdiceanddms) is a weekly Australian podcast analysing Dungeons and Dragons as well as other role-playing games. Each week the hosts discuss a different topic concerning interactions at the table, monsters, or just general trends in the game.

[Code Programming Python](https://pixabay.com/photos/code-programming-python-1084923/) by [Johnson Martin](https://pixabay.com/users/JohnsonMartin-724525/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1084923) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1084923).
