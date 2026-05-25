---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 220}"
bulk: "2"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Stitched together from pieces of ghoul skin, this suit of *+1 hide armor* grants you a +1 item bonus to saving throws against curses and makes you immune to the stench of ghouls. Ghoul hide with a resilient rune increases the resilient rune's item bonus to saving throws against curses by 1 (maximum +4).

**Source:** `= this.source` (`= this.source-type`)
