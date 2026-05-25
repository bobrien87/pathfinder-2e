---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 1900}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This staff is topped with carved animal and monster heads. While wielding the staff, you gain a +2 circumstance bonus to Nature checks to identify animals.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Know the Way]]

- **1st** [[Runic Body]] [[Summon Animal]]

- **2nd** [[Animal Messenger]] [[Speak with Animals]] [[Summon Animal]]

- **3rd** [[Animal Form]] [[Summon Animal]]

- **4th** [[Summon Animal]]

- **5th** [[Animal Form]] [[Moon Frenzy]] [[Summon Animal]]

**Craft Requirements** Supply one casting of all listed levels of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
