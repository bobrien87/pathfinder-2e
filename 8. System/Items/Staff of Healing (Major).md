---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 1800}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This white wood staff is capped at each end with a golden cross adorned with ruby cabochons. A *staff of healing* grants a +3 item bonus to the Hit Points you restore anytime you cast the *heal* spell using your own spell slots or charges from the staff.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Stabilize]]
- **1st** [[Heal]]
- **2nd** [[Clear Mind]] [[Heal]] [[Sound Body]]
- **3rd** [[Cleanse Affliction]] [[Heal]]
- **4th** [[Cleanse Affliction]] [[Clear Mind]] [[Sound Body]]
- **5th** [[Breath of Life]] [[Heal]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
