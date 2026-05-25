---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A miniature ingot of metal hangs upon a leather cord, with deep weapon grooves on its surface. A weapon it's applied to counts as cold iron for physical damage it deals for 1 minute, depending on its type.

> [!danger] Effect: Transmuting Ingot

**Source:** `= this.source` (`= this.source-type`)
