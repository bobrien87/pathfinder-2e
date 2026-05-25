---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Inscribed]]"]
price: "{'sp': 15}"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Scroll robes are composed of paper alchemically treated for strength and flexibility. A layered structure prevents cutting and tearing, and for the purpose of calculating damage, the robes are considered to be cloth. The paper accepts all sorts of decoration, including magical writing, as detailed in the inscribed trait.

**Source:** `= this.source` (`= this.source-type`)
