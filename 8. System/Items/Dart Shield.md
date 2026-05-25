---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Launching dart]]"]
price: "{'gp': 8}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wooden shield features a spring-loaded device on its surface that can fire darts with powerful force. A small mechanism within the shield allows you to fire a dart even while actively holding the shield or blocking with it.

**Source:** `= this.source` (`= this.source-type`)
