---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Combination]]", "[[Deadly d8]]", "[[Monk]]"]
price: "{'gp': 8}"
usage: "held-in-one-plus-hands"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The bow staff is a whipstaff with a retracting spool of wire inside a metal cap on one end and a hooked protrusion on the other. A wielder trained in the weapon's use can quickly spool and attach or detach the wire to transition the weapon between bow and staff functionality.

**Source:** `= this.source` (`= this.source-type`)
