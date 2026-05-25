---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 20, 'pp': 0, 'sp': 0}"
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

This metal disk is engraved with an image of an open eye, which always seems to look directly at the creature viewing it no matter what angle it's seen from. The first time you succeed at a Strike against a given creature with a weapon under the effect of an *analysis eye*, as a free action, you learn one weakness or resistance of that creature; if the creature has multiple weaknesses or resistances, the GM selects which one you learn.

**Source:** `= this.source` (`= this.source-type`)
