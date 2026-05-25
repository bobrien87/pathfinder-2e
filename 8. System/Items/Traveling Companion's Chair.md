---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Barding]]", "[[Companion]]"]
price: "{'gp': 4}"
usage: "other"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This more robust assembly is well suited for longer travel and all manner of adventuring. As with the traveler's chair, small mechanisms built into the wheels and support struts allow the user to traverse up and down stairs without any additional difficulty (though moving up stairs is still difficult terrain, just like for other adventurers) and move without additional difficulty through ladders, uneven ground, and other common adventuring terrain.

**Source:** `= this.source` (`= this.source-type`)
