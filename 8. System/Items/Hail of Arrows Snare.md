---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 1500}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When a creature enters the snare's square, it releases hundreds upon hundreds of carefully prepared arrows, blanketing a @Template[emanation|distance:20]{20-foot radius} around the snare's square with massive arrow fire that deals @Damage[18d6[piercing]|options:area-damage] damage. Creatures in the area must attempt a [[Reflex]] save.

**Source:** `= this.source` (`= this.source-type`)
