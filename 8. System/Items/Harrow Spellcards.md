---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Grimoire]]", "[[Magical]]"]
price: "{'gp': 425}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Crafted of sturdy paper, each card of this harrow deck showcases a beautiful watercolor illustration with space to inscribe a spell below. When shuffled, its cards seem to fly between one another of their own accord.

**Activate** `pf2:f` (concentrate, fortune)

**Frequency** once per day

**Trigger** Your last action was to cast a spell prepared from this grimoire that has the detection, prediction, revelation, or scrying trait

**Effect** You draw forth a card to gain insight into future challenges you'll face. Draw a card from a harrow deck or roll 1d6:

1 = hammers (Athletics)

2 = keys (Acrobatics)

3 = shields (Survival)

4 = books (any Recall Knowledge)

5 = stars (Religion)

6 = crowns (Diplomacy).

The next time you attempt a check of the same type as your result, roll twice and take the better result, as the spirits of the harrow guide your actions. If not used by your next daily preparations, this benefit disappears.

**Source:** `= this.source` (`= this.source-type`)
