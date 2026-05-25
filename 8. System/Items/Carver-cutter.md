---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]", "[[Sweep]]", "[[Wood]]"]
price: "{'gp': 1400}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Many of the experienced woodcarvers of the Plane of Wood learn to fight as well, the better to travel into hazardous areas in search of rare and beautiful types of wood for their craft. A *carver-cutter* serves a dual role as a weapon and a tool for felling trees and engraving wood. The *+2 striking battle axe* looks like an exquisitely made woodcutting axe.

**Activate - Carving Chisel** `pf2:1` (concentrate, manipulate)

**Effect** You pull free a woodworking chisel stored in the knob of the axe. It can have any standard chisel shape you imagine as you activate this ability. You get a +2 item bonus to Crafting checks for woodworking if you use chisels from the *carver-cutter.* The chisel also functions as a main-gauche. All runes on the axe are replicated on the chisel, but only while both items are on the same person. You can Interact to reinsert the chisel.

**Activate - Chop Down** `pf2:2`

**Frequency** once per hour

**Effect** Make a Strike with the axe against a plant creature or a creature made primarily of wood. This Strike deals an additional 2d6 precision damage, and on a hit, the creature is [[Clumsy]] 1 for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
