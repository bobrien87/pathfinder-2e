---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Bulwark]]"]
price: "{'gp': 35}"
bulk: "4"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Hellknights wear a variety of armors decorated with designs specific to the order. Hellknight half plate is the armor of choice for Hellknight signifiers, and Hellknight breastplate serves those in the order who lack the training to wear heavy armor.

A character who is a member of the Hellknights has access to these uncommon armors.

**Source:** `= this.source` (`= this.source-type`)
