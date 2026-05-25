---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]", "[[Relic]]", "[[Water]]"]
price: "{'value': {}}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Little is known about the origins of this wintry cloak of snowflakes, which functions as a [[Living Mantle]] but with snow instead of plants.

**Source:** `= this.source` (`= this.source-type`)
