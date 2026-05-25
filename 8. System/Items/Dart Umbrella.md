---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Concealable]]", "[[Nonlethal]]"]
price: "{'gp': 1}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This umbrella fires tiny blowgun darts from its ferrule with a twist of the handle. The darts are loaded into the shaft, and though the damage they deal is minimal, the dart umbrella is an inconspicuous weapon easy to slip past inspections.

**Source:** `= this.source` (`= this.source-type`)
