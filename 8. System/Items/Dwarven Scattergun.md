---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Concussive]]", "[[Dwarf]]", "[[Kickback]]", "[[Scatter 10]]"]
price: "{'gp': 10}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A favored weapon of dwarf scouts from Dongun Hold, the dwarven scattergun is a powerful weapon designed to take advantage of a dwarf's sturdy frame. A dwarven scattergun fires a large paper cartridge stuffed with black powder and knuckle-sized lumps of metal, creating a devastating burst so destructive that a foolish dwarf might find themself catching painful ricochets when firing at a too-close target. Some scatterguns are crafted with a clockwork firing tray that can quickly sort and load black powder and shot without needing a prepackaged cartridge, though this is largely an aesthetic feature with no real mechanical benefit.

**Source:** `= this.source` (`= this.source-type`)
