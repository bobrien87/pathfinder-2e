---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 230}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A glass orb atop this metal staff contains fine sand. While wielding the staff, you gain a +2 circumstance bonus to Perception checks to identify morph and polymorph magic.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **1st** [[Pest Form]]

- **2nd** [[Animal Form]], [[Enlarge]], [[Shrink]]

**Craft Requirements** Supply one casting of all listed levels of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
