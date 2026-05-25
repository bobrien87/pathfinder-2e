---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Healing]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 400, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A set of *leeching fangs* is a metal sculpture in the form of a fanged maw, and when applied to a weapon, it causes the weapon or its ammunition to grow numerous mouths filled with serrated teeth. *Leeching fangs* establish a metaphysical link between the life force of the wielder of the weapon it's applied to and those it damages. Whenever you deal Hit Point damage to a living creature with a weapon under the effect of *leeching fangs*, you heal yourself half the amount of Hit Point damage dealt. This cannot heal you above your maximum number of Hit Points.

**Source:** `= this.source` (`= this.source-type`)
