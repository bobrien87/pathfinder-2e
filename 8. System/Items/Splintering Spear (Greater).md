---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Magical]]", "[[Monk]]", "[[Thrown 20]]", "[[Wood]]"]
price: "{'gp': 15000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The entirety of this *+3 high-grade duskwood greater striking spear* is made of worn, cracked, splintered wood, including the spearhead. These splinters never harm you when you hold the weapon, but when you hit with the spear, splinters break off in the target, dealing 1d6 bleed damage.

**Activate—Shatter** `pf2:2`

**Frequency** once per day

**Effect** You smash the spear into the ground or another nearby surface, shattering it into thousands of duskwood splinters in your choice of a @Template[cone|distance:30] or a @Template[emanation|distance:10]. Each creature in the area takes @Damage[16d6[piercing]|options:area-damage] damage with a DC 37 [[Reflex]] save. A creature that fails also takes the same amount of persistent bleed damage as the spear deals on a hit. The spear regrows into its full form at the end of this turn.

**Source:** `= this.source` (`= this.source-type`)
