---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Healing]]", "[[Magical]]", "[[Potion]]", "[[Vitality]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

A *healing potion* is a vial of a ruby-red liquid that imparts a tingling sensation as the drinker's wounds heal rapidly. When you drink a *healing potion*, you regain 1d8 healing Hit Points.

**Source:** `= this.source` (`= this.source-type`)
