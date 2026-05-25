---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Combination]]", "[[Concussive]]", "[[Fire]]", "[[Kickback]]", "[[Magical]]"]
price: "{'gp': 700}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This black obsidian blade is a *+1 striking flaming gun sword*. Magma seeps along its many cracks and crags, and the handle is hot but not scalding to the touch.

**Activate—Explosion of Shards** `pf2:1` (manipulate)

**Requirements** Your most recent action this turn was a successful ranged Strike with *greater obsidian edge*

**Frequency** once per 10 minutes

**Effect** Magma coats the sword blade completely before exploding from your weapon in a @Template[emanation|distance:15] of fire and glass. Creatures in the area take @Damage[3d6[fire],2d6[piercing]|options:area-damage]{3d6 fire damage and 2d6 piercing damage} with a DC 25 [[Reflex]] save.

**Source:** `= this.source` (`= this.source-type`)
