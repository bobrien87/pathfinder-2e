---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Clockwork]]", "[[Consumable]]", "[[Fire]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 25}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The snare takes the form of a Tiny, drake-like clockwork toy. When a creature enters its square the snare activates, causing the drake to spit a gout of fire in a @Template[type:cone|distance:15] in the direction from which the creature entered. For instance, if a creature entered the square coming from the east, the cone would point east, to hit any allies behind the triggering creature. Those within the cone take @Damage[6d6[fire]|options:area-damage] damage with a DC 19 [[Reflex]] save. After spitting its fire, the snare falls apart

**Source:** `= this.source` (`= this.source-type`)
