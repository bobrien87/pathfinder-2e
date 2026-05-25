---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Deadly d8]]", "[[Forceful]]", "[[Sweep]]", "[[Versatile b]]"]
price: "{'gp': 12}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A fusion of a naginata and sansetsukon, this three-section weapon has a sweeping, curved blade along each of the outer sections. Though difficult for anyone but an expert weapon master to use effectively, the three-section naginata can be wielded at devastating speed to slice or smash apart a foe.

**Source:** `= this.source` (`= this.source-type`)
