---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Bulwark]]", "[[Laminar]]"]
price: "{'gp': 35}"
bulk: "5"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Larger plates coupled with lamellar pieces to make up a suit of heavy lamellar. The custom-fitted and often highly decorative suit covers most of the body. Rounding out the suit are a tiered helmet and fearsome mask, often depicting a fiendish or monstrous creature.

**Source:** `= this.source` (`= this.source-type`)
