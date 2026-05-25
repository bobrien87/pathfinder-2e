---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]"]
price: "{'gp': 100}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Duration** 1 week

A ghost delivery fulu's inscription resembles a dovecote with spirits around it, and it has a prominent stamp in red wax. This fulu activates once affixed, becoming the homing location of ghost courier fulus with a matching stamp. Delivered ghost courier fulu messages stick to the ghost delivery fulu but can be easily removed.

**Source:** `= this.source` (`= this.source-type`)
