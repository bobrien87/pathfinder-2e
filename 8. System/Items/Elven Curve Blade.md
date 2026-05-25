---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Elf]]", "[[Finesse]]", "[[Forceful]]"]
price: "{'gp': 4}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Essentially a longer version of the scimitar, this traditional elven weapon has a thinner blade than its cousin.

**Source:** `= this.source` (`= this.source-type`)
