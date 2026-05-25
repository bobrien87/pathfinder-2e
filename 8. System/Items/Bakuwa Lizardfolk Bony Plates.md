---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Aquadynamic]]", "[[Comfort]]"]
price: "{'value': {}}"
bulk: "—"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Note** Bakuwa Lizardfolk heritage only

Your plates are medium armor in the plate armor group that grant a +4 item bonus to AC, a Dex cap of +1, a check penalty of –2, a Speed penalty of –5 feet, a Strength value of +3, and have the aquadynamic and comfort traits. You can never wear other armor or remove your plates. You can etch armor runes onto your plates.

**Source:** `= this.source` (`= this.source-type`)
