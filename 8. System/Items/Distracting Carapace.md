---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 80}"
usage: "implanted"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Your skin is studded with pieces of iridescent chitin that ripple like oil on water. When you move your body in a distracting way, your allies can take advantage to move stealthily. When you [[Aid]] an ally who is trying to [[Create a Diversion]], instead of the usual effects of Aid, you can roll an Acrobatics or Performance check and use that result to determine the outcome of the diversion, instead of attempting a Deception check.

**Source:** `= this.source` (`= this.source-type`)
