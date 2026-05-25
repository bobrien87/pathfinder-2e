---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Razing]]", "[[Reach]]", "[[Shove]]", "[[Versatile b]]"]
price: "{'gp': 4}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A bec de corbin is a spiked polearm that uses a hammer head to help balance the spike. The hammer portion can be used as a secondary striking surface, while the spike or fluke is specially designed to punch through armor and shields.

**Source:** `= this.source` (`= this.source-type`)
