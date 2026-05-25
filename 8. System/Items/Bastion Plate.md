---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Bulwark]]", "[[Entrench melee]]", "[[Hindering]]"]
price: "{'gp': 33}"
bulk: "5"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This cumbersome and sturdy plate armor has fluting and additional protection built into the cuirass, helm, pauldrons, and vambraces. Bastion plate was invented for protection in combat tournaments meant to be sporting rather than lethal.

**Source:** `= this.source` (`= this.source-type`)
