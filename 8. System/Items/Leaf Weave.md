---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Laminar]]"]
price: "{'gp': 4}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Specialized crafters, often elves, create leaf weave out of sturdy leaves from ancient or magically enriched trees. Such leaves, when treated properly, have the strength of leather, and other tough plant materials hold the leaves together to form the armor. Such suits are popular among those who wish to avoid materials taken from slain beasts. As a material, leaf weave has the same statistics as thin wood.

**Source:** `= this.source` (`= this.source-type`)
