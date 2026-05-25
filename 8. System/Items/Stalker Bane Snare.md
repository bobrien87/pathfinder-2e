---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 15}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This snare explodes in a burst of cloying powder that can cling to a creature stepping into its square. A creature that enters the square of a stalker bane snare must attempt a [[Reflex]] save.
- **Critical Success** The target is unaffected.
- **Success** Powder sticks to the target, causing it to leave behind telltale footprints. Being [[Invisible]] makes the target [[Hidden]], rather than [[Undetected]], to creatures that could see it if it weren't invisible.
- **Failure** Powder clumps on the target, constantly flaking away. Being invisible makes the target [[Concealed]], rather than hidden or undetected, to creatures that could see it if it weren't invisible.
- **Critical Failure** As failure, and the creature is [[Blinded]] until the end of its next turn.

**Source:** `= this.source` (`= this.source-type`)
