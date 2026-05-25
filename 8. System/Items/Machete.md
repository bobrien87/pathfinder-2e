---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Deadly d8]]", "[[Sweep]]"]
price: "{'sp': 7}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This medium-length sword has a wide, gently curved blade and long grip. Though it's typically used to hack through heavy foliage, the machete can also be used as a deadly weapon.

**Source:** `= this.source` (`= this.source-type`)
