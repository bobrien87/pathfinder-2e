---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 4}"
usage: "wornclothing"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Desert clothing is made up of loose-fitting, light, breathable clothes that protect your head and body from the sun and allow you to cool off easily. They allow you to negate the damage from severe environmental heat and reduce the damage from extreme heat to that of severe heat. This effect is negated if the clothing is worn with any armor, except armor that is especially cooling at the GM's discretion.

**Source:** `= this.source` (`= this.source-type`)
