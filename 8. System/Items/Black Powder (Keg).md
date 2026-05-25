---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "50"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Black powder is a volatile and explosive alchemical substance commonly used in the production of firearm munitions. Black powder becomes inert and useless when wet and must be kept in a sealed, water-tight container.

A keg contains 5,000 doses of black powder and can be detonated in the same way as a horn. As long as the keg is mostly full (at least 4,000 doses remaining) this deals @Damage[3d6[fire]|options:area-damage] damage in a @Template[type:burst|distance:20] (DC 20 [[Reflex]] save). Detonating multiple kegs can increase the area, but not the damage, of this effect; detonating a keg and any horns at the same time in an overlapping area also doesn't increase the damage.

**Source:** `= this.source` (`= this.source-type`)
