---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Comfort]]"]
price: "{'gp': 3}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Quilted armor is built in a long coat intended for defensive use without other armor. Quilted armor protects the upper body and legs, differentiating it further from the typical padded undercoat. This armor is frequently made in stylish colors or patterns to facilitate use as protective outerwear or a military uniform.

**Source:** `= this.source` (`= this.source-type`)
