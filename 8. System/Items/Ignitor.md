---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Clockwork]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An ignitor uses interlocking clockwork to create a small spark in order to ignite flammable materials. While holding the ignitor, you can Interact with it to ignite a flammable object within reach.

**Source:** `= this.source` (`= this.source-type`)
