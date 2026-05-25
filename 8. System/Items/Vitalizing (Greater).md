---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]"]
price: "{'gp': 4300}"
usage: "etched-onto-melee-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *greater vitalizing* weapon pulses with vital energy, dealing an extra 2d6 persistent vitality damage to undead.

On a critical hit, the undead creature is [[Enfeebled]] 1 and [[Stupefied 1]] as long as it has the persistent damage from this rune.

**Source:** `= this.source` (`= this.source-type`)
