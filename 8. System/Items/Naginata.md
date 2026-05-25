---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Deadly d8]]", "[[Reach]]", "[[Versatile p]]"]
price: "{'gp': 3}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This 6-foot staff has a 2-foot-long, slightly curved, swordlike blade attached at one end. The long pole helps keep the wielder out of reach of swords and shorter weapons.

**Source:** `= this.source` (`= this.source-type`)
