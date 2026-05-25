---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Finesse]]", "[[Tethered]]", "[[Thrown 20]]", "[[Training]]"]
price: "{'gp': 2}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A combat lure is a weighted leather sack at the end of a length of toughened cord and can be used both to bludgeon opponents and signal directions to a trained avian or other animal.

**Source:** `= this.source` (`= this.source-type`)
