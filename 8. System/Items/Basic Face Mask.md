---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 3}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This simple cloth mask, sewn to closely fit your face, is fastened by two sets of strings drawn across your face and secured behind your head. While wearing the mask, you gain a +1 item bonus on any initial saves to avoid contracting airborne diseases, such as choking death or tuberculosis.

**Source:** `= this.source` (`= this.source-type`)
