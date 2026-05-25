---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Electricity]]", "[[Gadget]]"]
price: "{'gp': 180}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This glass orb has a Stasian coil in the center, allowing visible electricity to be safely seen within the glass. The electricity that dances within this orb can be transferred to the user of this gadget, allowing their muscles to react and respond much quicker. When activated, you gain a +2 circumstance bonus to Reflex saves and AC for 1 minute, or until you are hit by an attack or fail a Reflex saving throw, whichever happens first.

> [!danger] Effect: Static Muscular Relay

**Source:** `= this.source` (`= this.source-type`)
