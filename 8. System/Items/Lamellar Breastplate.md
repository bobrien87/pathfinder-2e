---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Hindering]]", "[[Laminar]]"]
price: "{'gp': 7}"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Slats of lacquered steel or other metal held together with cord, whether leather or silk, make up most lamellar breastplates. The lacquering prevents the metal from corroding.

**Source:** `= this.source` (`= this.source-type`)
