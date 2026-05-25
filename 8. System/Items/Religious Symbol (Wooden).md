---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 1}"
usage: "other"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This piece of wood or silver is emblazoned with an image representing a deity. Some divine spellcasters, such as clerics, can use a religious symbol of their deity to use certain abilities and cast some spells. A religious symbol can be worn on the body on a chain or pin, or can be held.

**Source:** `= this.source` (`= this.source-type`)
