---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Razing]]", "[[Shove]]", "[[Two hand d10]]", "[[Versatile p]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This massive hammer's metal head is shaped or molded with heavy metal wedges along its primary striking surface, enabling it to tear through shields and armor with ease.

**Source:** `= this.source` (`= this.source-type`)
