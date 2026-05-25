---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Gadget]]", "[[Magical]]"]
price: "{'gp': 400}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

A portable seal is a stiff framework of copper wires and strategically placed hinges, so that when the device is snapped open it forms an instant geometric design. A tiny Stasian coil is attached, which when activated runs a mixture of occult energy and high-voltage electricity through the wire. The design covers a @Template[type:burst|distance:5] when unfolded and must be unfolded into an area free of major obstructions such as rocks or hostile creatures. When a creature with the summoned trait attempts to enter the seal's area or make a melee Strike against a creature in that area, the summoned creature must attempt a DC 28 [[Will]] save.
- **Success** The action occurs normally, and the creature is immune to the effects of this portable seal this round.
- **Failure** The movement or Strike is disrupted, but the creature is immune to further effects of the portable seal this round.
- **Critical Failure** The movement or Strike is disrupted.

**Source:** `= this.source` (`= this.source-type`)
