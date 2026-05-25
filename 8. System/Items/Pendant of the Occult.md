---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Occult]]"]
price: "{'gp': 60}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This amulet is hollow and shaped in the form of an unblinking eye. Its cavity typically holds some fragment of occult text. While wearing the pendant, you gain a +1 item bonus to Occultism checks, and you can cast the [[Guidance]] cantrip as an occult innate spell.

**Source:** `= this.source` (`= this.source-type`)
