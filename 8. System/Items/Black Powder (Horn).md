---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "5"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Black powder is a volatile and explosive alchemical substance commonly used in the production of firearm munitions. Black powder becomes inert and useless when wet and must be kept in a sealed, water-tight container.

A horn contains 500 doses worth of black powder. A horn can be detonated by leaving a small trail of black powder and then lighting it. Each 5-foot square requires one dose of black powder to create a trail through. As long as the horn is mostly full (at least 400 doses remaining) it can be detonated to deal @Damage[1d6[fire]|options:area-damage] damage in a @Template[type:burst|distance:5] (DC 16 [[Reflex]] save). It takes 1 round per 15 feet of powder trail laid down for a horn to detonate after the trail is lit. If multiple horns detonate simultaneously, it can increase the area of the explosion, but the damage in overlapping areas doesn't increase.

**Source:** `= this.source` (`= this.source-type`)
