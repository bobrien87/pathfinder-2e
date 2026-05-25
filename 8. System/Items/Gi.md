---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Comfort]]"]
price: "{'sp': 2}"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Also called martial arts suits or practice clothes, gi are outfits of tough cloth built for comfort and unrestricted movement—ideal for practicing martial arts. They have reinforced stitching resistant to strenuous use.

**Source:** `= this.source` (`= this.source-type`)
