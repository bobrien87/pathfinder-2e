---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Comfort]]"]
price: "{'value': {}}"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Note** Hardshell Surki heritage only

Your carapace is medium armor in the plate armor group that grants a +4 item bonus to AC, a Dex cap of +1, a check penalty of –2, a Speed penalty of –5 feet, a Strength value of +3, and has the comfort trait. You can never wear other armor or remove your carapace. You can etch armor runes onto your carapace.

**Source:** `= this.source` (`= this.source-type`)
