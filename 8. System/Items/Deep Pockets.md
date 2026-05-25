---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 220}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 leather armor* has two medium-sized pockets just above the waist where you might normally place your hands if they were cold. Each pocket is covered with a leather flap that surprisingly remains closed even with dynamic movement and heavy winds. Each individual pocket functions as a [[Spacious Pouch (Type I)]].

**Craft Requirements** The initial raw materials must include two *type I spacious pouches*.

**Source:** `= this.source` (`= this.source-type`)
