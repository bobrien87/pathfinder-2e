---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 70}"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This peculiar ammunition is coated in yellow dust that leaves a stain on anything it touches. When activated corrosive ammunition hits a target, it dissolves across the target's armor. The armor takes 1d8 persistent,acid damage that ignores the armor's Hardness; if the target isn't wearing armor, it takes the acid damage instead. This damage occurs at the end of the target's turns.

The creature can end this effect by spending an Interact action to wipe off the corrosive dust, and otherwise the effect ends once the armor becomes broken.

**Source:** `= this.source` (`= this.source-type`)
