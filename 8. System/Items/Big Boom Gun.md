---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Cobbled]]", "[[Fatal d12]]", "[[Goblin]]", "[[Modular]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Developed by a goblin weaponsmith who missed the "hand" part of "hand cannon," this comically oversized gun has a heavily reinforced barrel and is loaded with a worrisome quantity of gunpowder. This hand cannon is a martial weapon instead of a simple weapon. It has the fatal d12 trait and a range increment of 20 feet. It also has the following modified critical failure condition.
- **Critical Failure** The attack misses, the weapon misfires, and you take 1d12 fire damage as it explodes in your face.

**Source:** `= this.source` (`= this.source-type`)
