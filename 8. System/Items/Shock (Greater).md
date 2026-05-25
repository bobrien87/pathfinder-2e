---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Electricity]]", "[[Magical]]"]
price: "{'gp': 6500}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Electric arcs crisscross *shock* weapons, dealing an extra 1d6 electricity damage on a hit. On a critical hit, electricity arcs out to deal an equal amount of electricity damage to up to two other creatures of your choice within 10 feet of the target.

Electricity damage dealt by this weapon ignores the target's electricity resistance (and the other creatures' on a critical hit).

**Source:** `= this.source` (`= this.source-type`)
