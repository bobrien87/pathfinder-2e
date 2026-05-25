---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 14}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

You sprinkle these salts onto a single object up to 10 cubic feet in volume and no more than 40 Bulk to preserve it for 1 week. The object doesn't decay, and effects that require the object to be fresh don't count the time passing during this duration as having elapsed. When sprinkled on a corpse, this extends the period in which a creature can be revived by magic, as well as the wait time required before a corpse can be targeted again with [[Talking Corpse]]. The salts prevent ordinary pests from consuming the target (such as maggots for a corpse or moths for a piece of clothing). Any creature can use an Interact action to disperse the salts from an unattended object and end this effect.

**Source:** `= this.source` (`= this.source-type`)
