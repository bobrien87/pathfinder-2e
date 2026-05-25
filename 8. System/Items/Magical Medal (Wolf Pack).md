---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 350}"
usage: "worn"
bulk: "—"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Military leaders or heads of state award these special medals to commend exemplary performance by their top soldiers. They're typically worn on a special strip of fabric near the lapel, but soldiers from different countries sometimes wear them in other places. No matter how many magical medals you have, they collectively count as one invested item.

There are three wolf's heads engraved on this pewter medal, typically awarded to squads who demonstrate exceptional teamwork. While wearing the medal of the wolf pack, you gain a +2 circumstance bonus to damage rolls against enemies you are flanking.

**Source:** `= this.source` (`= this.source-type`)
