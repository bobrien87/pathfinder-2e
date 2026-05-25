---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Reach]]", "[[Trip]]"]
price: "{'gp': 2}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This polearm bears a long, often one-sided, curved blade with a hook protruding from the blunt side of the blade, which can allow its wielder to trip opponents at a distance. Its shaft is usually 8 feet long.

**Source:** `= this.source` (`= this.source-type`)
