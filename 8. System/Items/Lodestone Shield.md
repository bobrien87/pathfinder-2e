---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]"]
price: "{'gp': 1350}"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *moderate reinforcing cold iron shield* (Hardness 10, HP 92, BT 46) is inset with lodestones that draw ammunition toward it.

**Activate—Attract Projectile** R (manipulate)

**Frequency** once per minute

**Trigger** A ranged weapon Strike targets a creature within 15 feet of you when you have this shield raised, and the attacker hasn't yet rolled their attack

**Effect** The triggering Strike targets you instead of its normal target. If it hits, you gain the effects of the Shield Block reaction.

**Source:** `= this.source` (`= this.source-type`)
