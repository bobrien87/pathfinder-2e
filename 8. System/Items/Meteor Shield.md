---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Shield throw 30]]"]
price: "{'gp': 4}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Meteor shields are specifically designed with throwing in mind. A meteor shield is made from thin steel and has quick-release straps, allowing for easy, long-distance throws.

**Source:** `= this.source` (`= this.source-type`)
