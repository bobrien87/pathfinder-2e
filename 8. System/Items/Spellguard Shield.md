---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]"]
price: "{'gp': 250}"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This shield bears eldritch glyphs to guard against magic. While you have this steel shield (Hardness 6, HP 24, BT 12) raised, you gain its circumstance bonus to saving throws against spells that target you (as well as to AC), and you can Shield Block spells that target you if you have that action.

**Source:** `= this.source` (`= this.source-type`)
