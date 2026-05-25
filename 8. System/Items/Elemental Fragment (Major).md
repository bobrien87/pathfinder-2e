---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 500}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate, manipulate)

This chunk of solidified planar energy is as large as a walnut and comes in six different varieties: a clear piece of crystal for the Plane of Air, a rough piece of rock for the Plane of Earth, a solidified piece of cooled lava for the Plane of Fire, a compact piece of iron for the Plane of Metal, a solid piece of ice for the Plane of Water, or a compact mass of plant matter for the Plane of Wood. You crack the fragment as you activate it, unleashing the planar energy within. This energy casts a spell of your choice: a 7th-rank [[Elemental Form]] spell affecting you or a 7th-rank [[Summon Elemental]] spell; if you summon an elemental, you can Sustain the activation to keep control of the elemental. The spell's element matches that of the fragment.

**Source:** `= this.source` (`= this.source-type`)
