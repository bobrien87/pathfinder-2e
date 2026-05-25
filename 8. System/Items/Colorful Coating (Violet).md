---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 15}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:3` (manipulate)

These coatings come in different colors, each with a different special effect. A bottle of colorful coating contains enough to slather over one 5-foot square within your reach or space and is made with a special dispenser that enables you to coat the surface using only one hand. It's possible to use the coating on any surface that can be painted (subject to the GM's discretion). Colorful coating dries instantly, and its effect in the square you coated lasts for 1 minute. After that time, the coating turns to fine, inert powder, returning the square to its original condition unless otherwise noted.

Violet colorful coating contains compounds that become goopy and sticky. A square of this coating is difficult terrain. Any creature that enters the square must succeed at a DC 20 [[Reflex]] save or take a –15-foot penalty to its Speeds until the end of its next turn. On a critical failure, the creature is [[Immobilized]] in the square until the end of its next turn. The target can end these effects by [[Escaping]] (DC 20) or spending 2 Interact actions to remove the sticky substances. These Interact actions don't have to be consecutive, and other creatures can help by providing the actions.

**Source:** `= this.source` (`= this.source-type`)
