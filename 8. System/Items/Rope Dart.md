---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Disarm]]", "[[Finesse]]", "[[Sweep]]", "[[Tethered]]", "[[Thrown 20]]", "[[Trip]]"]
price: "{'gp': 1}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A deceptively simple weapon made from a length of cord attached to a weighted, conical metal spike. A rope dart can be whirled and manipulated at great speeds to attack in unexpected ways and from unexpected angles.

**Source:** `= this.source` (`= this.source-type`)
