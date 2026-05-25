---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]"]
price: "{'gp': 160}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wooden baton is carved with a vine design that spirals from one end of the rod to the other. Similar batons were used by Taldan commanders of their Armies of Exploration for thousands of years.

**Activate—Forward March!** `pf2:2` (manipulate, visual)

**Frequency** once per day

**Effect** You brandish the *vine baton* with a flourish or in some other dramatic manner. You and your allies within 120 feet can Hustle for 1 additional hour. If you enter an encounter during this time period, the effect ends, but you receive a +2 status bonus to your initiative rolls for that encounter.

> [!danger] Effect: Forward March!

**Source:** `= this.source` (`= this.source-type`)
