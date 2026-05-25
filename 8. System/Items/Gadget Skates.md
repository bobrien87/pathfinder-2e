---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Clockwork]]", "[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 21}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate, move)

Gadget skates are metal devices that come in pairs and strap onto existing footwear (or a creature's feet). When you Activate gadget skates, clockwork gears reveal small wheels that propel you along the ground, moving you up to twice your Speed. During this movement, you must succeed at a DC 20 [[Acrobatics]] check to turn up to 90 degrees, and you can't turn more than once or more than 90 degrees. During the activation and after the activation is complete, you can't Stride, Step, or otherwise move on the ground until the end of your next turn. However, you can use this movement instead of a Stride to perform a [[High Jump]] or [[Long Jump]] just after the activation ends, in the direction of your last movement using the gadget skates.

You can Sustain the Activation of your gadget skates for up to 1 minute. Starting on the turn after you Activate the gadget skates, the first time you Sustain the Activation each turn, you gain the effects of the activation again: you move up to twice your Speed in the same direction as your last movement with the gadget skates, and the restrictions continue to apply until you choose to cease Sustaining the Activation or you reach the maximum duration. Once the effect ends, the skates fall away and you can move normally.

**Source:** `= this.source` (`= this.source-type`)
