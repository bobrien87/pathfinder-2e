---
type: item
source-type: "Remaster"
level: "21"
traits: ["[[Agile]]", "[[Artifact]]", "[[Backstabber]]", "[[Deadly d8]]", "[[Divine]]", "[[Finesse]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #206: Bring the House Down"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Retribution is a *+3 greater striking keen shifting wounding war razor*.

**Activate—Vengeful Slice** `pf2:1` (manipulate)

**Frequency** once per round

**Effect** You make a Strike with Retribution against a target within 120 feet that you can see and who damaged you within the last minute, as if they were within reach.

**Source:** `= this.source` (`= this.source-type`)
