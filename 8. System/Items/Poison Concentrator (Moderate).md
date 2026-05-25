---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Alchemical]]"]
price: "{'gp': 960}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This compression apparatus can reduce two poisons into a more concentrated dose. As a 10-minute activity that has the manipulate trait, you can use a poison concentrator to combine two doses of the same infused alchemical poison of level 9 or lower. The concentrated poison has a +1 item bonus to its DC, and its level is increased by 1.

**Source:** `= this.source` (`= this.source-type`)
