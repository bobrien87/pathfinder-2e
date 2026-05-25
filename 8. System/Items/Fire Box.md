---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Clockwork]]", "[[Consumable]]", "[[Fire]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Anyone who opens the box triggers a clockwork mechanism that unleashes a @Template[type:cone|distance:15] of fire. The cone issues forth in a random direction determined by the GM but always including the creature who opened the box. Those within the cone take @Damage[4d6[fire]|options:area-damage] damage with a DC 17 [[Reflex]] save.

**Source:** `= this.source` (`= this.source-type`)
