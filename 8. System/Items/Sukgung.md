---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Fatal aim d12]]"]
price: "{'gp': 7}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The sukgung is an extremely efficient crossbow most common in the nation of Hwanggot. Capable of lethal shots at remarkable distances, the sukgung is well-balanced enough to be fired with one hand.

**Source:** `= this.source` (`= this.source-type`)
