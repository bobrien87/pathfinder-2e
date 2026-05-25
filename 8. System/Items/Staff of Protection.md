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

This wooden staff is remarkably sturdy and unyielding. While wielding the staff, you gain a +1 circumstance bonus to your DC to avoid being shoved or tripped.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Shield]]

- **1st** [[Alarm]], [[Mystic Armor]]

- **2nd** [[Dispel Magic]], [[Environmental Endurance]], [[Resist Energy]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
