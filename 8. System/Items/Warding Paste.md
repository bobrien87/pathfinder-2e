---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:3` (manipulate)

Silver filings to ward off fiends, cold iron filings to repulse demons and fey, and powders made from garlic, peppers, and wort to repel undead creatures are combined into this gritty paste. A container of warding paste contains enough to cover one suit of armor or set of clothes. For the next hour, creatures with the unholy trait take a -1 circumstance penalty to melee attacks against the affected outfit's wearer.

> [!danger] Effect: Warding Paste (Wearer)

**Source:** `= this.source` (`= this.source-type`)
