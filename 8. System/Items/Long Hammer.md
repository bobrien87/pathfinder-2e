---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Brace]]", "[[Dwarf]]", "[[Reach]]", "[[Trip]]", "[[Versatile p]]"]
price: "{'gp': 5}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The long hammer features a pronged hammer head designed for damaging knees and ankles, counterbalanced by a stout spike and affixed to a reinforced shaft between 5 and 7 feet long.

**Source:** `= this.source` (`= this.source-type`)
