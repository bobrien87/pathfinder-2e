---
type: item
source-type: "Remaster"
level: "2"
price: "{'gp': 35}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This thick mat of canvas, foliage, and wood is mounted on a tripod of flexible metal struts, folded into a baton-like shape, and clamped shut. You can rapidly deploy it on the ground with an Interact action to create cover. Deployable cover completely blocks one edge of the chosen square, allowing you (and others) to gain standard cover when you use the [[Take Cover]] action. Before it can be used again, deployable cover must be carefully folded and clamped shut, which takes 1 minute.

Specially crafted to protect against bullet fire, a ballistic cover also works against other physical projectiles, such as arrows, bolts, and thrown weapons. While a creature has cover from Taking Cover behind a ballistic cover, it gains resistance 2 to piercing damage from ranged weapons and ranged unarmed attacks.

**Source:** `= this.source` (`= this.source-type`)
