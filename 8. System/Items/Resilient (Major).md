---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Magical]]"]
price: "{'gp': 49440}"
usage: "etched-onto-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Resilient* runes imbue armor with additional protective magic. This grants the wearer a +3 item bonus to saving throws.

You can upgrade the *resilient* rune already etched on a suit of armor using the normal process for upgrading items and runes.

**Source:** `= this.source` (`= this.source-type`)
