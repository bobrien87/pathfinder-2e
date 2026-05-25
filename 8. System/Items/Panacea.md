---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Consumable]]", "[[Healing]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 450}"
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

This potion appears to shift colors, and no two observers describe it in the same way. When consumed, it attempts to counteract all curses and diseases affecting you, as well as the blinded and deafened conditions from spells affecting you. The potion has a counteract rank of 7 and a `r 1d20+20` modifier for the roll.

**Source:** `= this.source` (`= this.source-type`)
