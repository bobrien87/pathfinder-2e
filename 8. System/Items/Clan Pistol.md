---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Concussive]]", "[[Dwarf]]", "[[Fatal d10]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The tradition of dwarves displaying their clan affiliations with special clan daggers goes back millennia, but many of the dwarf clans of Dongun Hold have their own take on the tradition, with promising young gunsmiths claiming their adulthood by crafting a specialized personal firearm using the clan's unique smithing traditions. Losing or being forced to surrender their clan pistol is a terrible embarrassment for the dwarves that carry them.

**Source:** `= this.source` (`= this.source-type`)
