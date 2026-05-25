---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]"]
price: "{'gp': 480}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This leather pouch holds a pair of six-sided dice carved from actual knucklebones. When rolled, the dice grant you a vision of a distant location, though their power is unreliable.

**Activate—Roll the Bones** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You roll the dice. If you roll two 1s, the activation fails with no effect. Otherwise, the dice cast [[Clairvoyance]] for you. When cast in this way, the spell's range becomes 100 feet × the result of your roll.

**Source:** `= this.source` (`= this.source-type`)
