---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 13000}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

This oil contains energy that repels nearly all types of magic. When you apply this oil to armor, the creature wearing the armor becomes immune to all spells, effects of magic items (the wearer's and those of others), and effects with the magical trait for 1 minute.

The oil affects neither the magic of the armor nor the fundamental runes of weapons attacking the wearer. Magical effects from a source of 20th level or higher, such as a deity, still function on the armor's wearer.

**Source:** `= this.source` (`= this.source-type`)
