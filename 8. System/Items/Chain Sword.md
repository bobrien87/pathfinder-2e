---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Finesse]]", "[[Reach]]", "[[Sweep]]"]
price: "{'gp': 6}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This weapon has a hilt like a longsword attached to several bladed segments connected by chain links. A highly technical weapon, the chain sword is valued by duelists and experienced soldiers alike in the nations of Nirmathas and Molthune.

**Source:** `= this.source` (`= this.source-type`)
