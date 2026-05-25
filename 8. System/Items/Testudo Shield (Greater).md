---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]"]
price: "{'gp': 2800}"
bulk: "4"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This tower shield (Hardness 5, HP 20, BT 10) sports a bright red front with a gold inlay of an eagle. While it looks unassuming, this shield can protect not only yourself but also those behind you.

**Activate—Tortoise Form** `pf2:2` (concentrate, force, manipulate)

**Frequency** once per day

**Effect** Your shield creates a magical barrier, consisting of translucent copies of the shield. The wall is 1 inch thick, 25 feet long, and 10 feet high. The barrier is conjured adjacent to you in a straight line on the border between squares and lasts for 1 minute. The barrier is created with the Hardness and Hit Points equal to those of the testudo shield and is immune to critical hits and precision damage.

**Source:** `= this.source` (`= this.source-type`)
