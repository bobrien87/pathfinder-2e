---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Combination]]", "[[Concussive]]", "[[Elf]]", "[[Fatal d10]]", "[[Parry]]"]
price: "{'gp': 12}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A recently developed weapon created for an elven champion from Jinin, the three-peaked tree can be used as both a [[Trident]] and a [[Dawnsilver Tree]]. A three-peaked tree has a length of silken rope attached to the butt of its haft, allowing it to be quickly retrieved after thrown.

**Source:** `= this.source` (`= this.source-type`)
