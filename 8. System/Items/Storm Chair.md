---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Electricity]]", "[[Magical]]"]
price: "{'gp': 4400}"
usage: "worn"
bulk: "3"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This traveler's chair uses Stasian technology to ride lightning.

**Activate—Electroball** `pf2:2` (electricity, manipulate)

**Frequency** once per hour

**Effect** You create a ball of electricity around the chair, surrounding it in a damaging aura of electricity and using electromagnetism to briefly levitate. For 1 minute, you gain a fly Speed equal to your Speed and adjacent creatures that hit you with a melee attack, as well as creatures that touch or hit you with an unarmed attack, take 2d6 electricity damage each time. As normal, this applies to creatures who choose to touch you, not when you touch or attack another creature.

> [!danger] Effect: Storm Chair

**Activate—Ride the Lightning** `pf2:2` (electricity, manipulate)

**Frequency** once per day

**Effect** You release the majority of the stored up energy from your *storm chair*, devastating foes in a chain of electricity. This has the effects of [[Chain Lightning]] with a DC of 31 (DC 31 [[Reflex]] save).

**Source:** `= this.source` (`= this.source-type`)
