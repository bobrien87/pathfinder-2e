---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]"]
price: "{'gp': 160}"
usage: "etched-onto-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Magic wards deflect attacks. Increase the armor's item bonus to AC by 1. The armor can be etched with one property rune.

You can upgrade the *armor potency* rune already etched on a suit of armor using the normal process for upgrading items and runes.

**Craft Requirements** You are an expert in Crafting.

**Source:** `= this.source` (`= this.source-type`)
