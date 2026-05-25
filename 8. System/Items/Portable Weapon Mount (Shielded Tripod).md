---
type: item
source-type: "Remaster"
level: "5"
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "3"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Powerful firearms like the arquebus were originally used to defend fortifications or ships, mounted on casements or pintles to steady their aim and offset their recoil. More mobile means of stabilizing weapons with kickback were developed as firearms began to spread across the Inner Sea. The standard tripod takes an Interact action to deploy using one hand.

A shielded tripod resembles a squat shield on a tripod. You can deploy and retrieve a shielded tripod with an Interact action, as normal, but while a shielded tripod is in your square, you can use the [[Take Cover]] action to gain standard cover behind the tripod's shield. You can't use this cover to Hide or [[Sneak]], as normal for times when your cover still leaves your position obvious.

**Source:** `= this.source` (`= this.source-type`)
