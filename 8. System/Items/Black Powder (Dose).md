---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'cp': 1}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** round

**Activate** `pf2:1` (manipulate)

Black powder is a volatile and explosive alchemical substance commonly used in the production of firearm munitions. Black powder becomes inert and useless when wet and must be kept in a sealed, water-tight container.

The smallest unit of black powder that still has a simple use, a dose can be a simple package paper parcel around black powder or it can be packaged with a metal bullet or pellet to be used as ammunition. When ignited with a fuse or exposed to direct flame, a dose of black powder explodes. This isn't powerful enough to deal damage but makes a loud sound and could trigger further explosions. A fuse for a dose can be created with a few twists of paper and causes the dose to explode the round after it's lit.

**Source:** `= this.source` (`= this.source-type`)
