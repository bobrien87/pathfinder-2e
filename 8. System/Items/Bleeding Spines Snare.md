---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 320}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When a creature enters the square, thorny spines protrude out to stab it, dealing @Damage[8d8[piercing],2d8[bleed]]{8d8 piercing damage and 2d8 persistent bleed damage}. The creature must attempt a [[Reflex]] save. After the initial trigger, the spines retract and protrude again repeatedly for 1 minute, forcing any creature that enters the space or ends its turn in the space to take damage from the spines (attempting the same basic Reflex save).

**Source:** `= this.source` (`= this.source-type`)
