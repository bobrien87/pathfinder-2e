---
type: item
source-type: "Remaster"
level: "1"
price: "{'gp': 20}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This long, hollow tube is held in two hands and braced over the shoulder. Inside, it contains a small metal basket sized to hold alchemical bombs. A chute in the top delivers an alchemical bomb into the internal basket, while a lever on the underside pulls the basket back and locks it in place. Loading an alchemical bomb into a bomb launcher requires a single Interact action. With a pull of a trigger, the basket speeds forward, allowing you to Strike with the loaded alchemical bomb over long distances. Bombs fired with a bomb launcher have a range increment of 60 feet.

**Source:** `= this.source` (`= this.source-type`)
