---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]", "[[Poison]]"]
price: "{'gp': 55}"
usage: "implanted"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Your salivary glands are modified to be capable of spraying a deadly venom. You gain a poison spray unarmed ranged attack with a range increment of 10 feet that deals 1d4 poison damage. On a critical hit, the target is also [[Sickened]] 1.

**Source:** `= this.source` (`= this.source-type`)
