---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This small, clockwork torch device uses a trigger-operated sparker to ignite a flow of flammable gas, creating a short, hot flame capable of rapidly cauterizing wounds and helping to stop bleeding. The cauterizing torch is applied to yourself or an adjacent target. The target attempts an immediate flat check to end any persistent bleed effect with the lower DC for particularly effective assistance.

**Source:** `= this.source` (`= this.source-type`)
