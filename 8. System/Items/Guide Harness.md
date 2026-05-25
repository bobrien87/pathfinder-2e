---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Companion]]"]
price: "{'gp': 5}"
usage: "worn"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The grip of this guide harness fits comfortably in the hand. Guide harnesses are purpose-built for low-sight or blind adventurers who have guide animals. Usually fastened with side straps placed through a martingale, guide harnesses can be easily reconfigured to allow them to be worn by any animal companion.

**Source:** `= this.source` (`= this.source-type`)
