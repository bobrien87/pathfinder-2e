---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Deflecting physical ranged]]"]
price: "{'gp': 6}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This specialized steel shield features an outer layer of angled wooden or steel plates, which help deflect or redirect incoming ranged projectiles but don't offer any additional protection against melee weapons.

**Source:** `= this.source` (`= this.source-type`)
