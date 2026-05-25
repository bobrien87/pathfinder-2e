---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Laminar]]"]
price: "{'gp': 5}"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Erutaki communities deep in the Crown of the World, where wood is hard to come by, fashion armor from slats and strips of bone or horn, along with whole bones or horns. Wealthier wearers sometimes pay for decorative embellishments made of more precious materials. Niyaháat is usually woven together with strong cord, forming a suit like a breastplate. This suit is worn over heavy clothing or a surcoat like padded armor. Some suits incorporate parts of powerful creatures, creating a storied history for the suit and its wearers.

**Source:** `= this.source` (`= this.source-type`)
