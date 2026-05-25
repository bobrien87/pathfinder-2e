---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Concealable]]", "[[Finesse]]", "[[Thrown 10]]"]
price: "{'sp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A favored self-defense weapon among bar and tavern workers, the corset knife has a weighted hilt and a cylindrical, needlelike blade designed to be easily hidden in clothing, but quickly retrieved in a pinch.

**Source:** `= this.source` (`= this.source-type`)
