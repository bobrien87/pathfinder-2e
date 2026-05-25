---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Combination]]", "[[Concussive]]", "[[Fatal d10]]"]
price: "{'gp': 10}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This item, favored by firearms-using dwarves and barbarians, takes the form of a sturdy musket that combine the functionality of melee weapons and with an axe blade attached near the muzzle.

**Source:** `= this.source` (`= this.source-type`)
