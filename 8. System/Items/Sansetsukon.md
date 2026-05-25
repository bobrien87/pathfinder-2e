---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Backswing]]", "[[Disarm]]", "[[Monk]]", "[[Parry]]"]
price: "{'gp': 2}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The sansetsukon, also known as a sanjiegun or three-section staff, is made up of three wooden staff segments, each about 14 inches in length. The staff sections are connected by short lengths of cord or chain, similar to nunchaku.

**Source:** `= this.source` (`= this.source-type`)
