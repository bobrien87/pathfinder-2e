---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Earth]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 500}"
bulk: "2"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 fire-resistant hide armor* is adorned with the shale-like scales of the zetogeki, a giant reptile that dwells near sites of volcanic activity. Like the armor's namesake, you can adjust the scales to better absorb kinetic energy at the cost of some mobility.

**Activate—Shift Scales** `pf2:1`

**Frequency** once per day

**Effect** Until the end of your next turn, you gain resistance 5 to bludgeoning, piercing, and slashing damage, but your Speeds are reduced by 10 feet (minimum 5 feet).

> [!danger] Effect: Shift Scales

**Source:** `= this.source` (`= this.source-type`)
