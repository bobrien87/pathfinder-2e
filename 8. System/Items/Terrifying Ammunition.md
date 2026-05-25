---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Emotion]]", "[[Fear]]", "[[Magical]]", "[[Mental]]"]
price: "{'gp': 50}"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This black-and-gray ammunition is etched with occult symbols and tiny, grinning skulls. When activated terrifying ammunition damages a creature, it fills the creature's mind with visions of their own failures, tragedies, and eventually, their own death. The creature must attempt a DC 20 [[Will]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Frightened]] 1.
- **Failure** The creature is [[Frightened]] 1 and can't reduce its frightened value below 1 until it spends an action, which has the concentrate trait, to calm itself down.
- **Critical Failure** As failure, but the creature is [[Frightened]] 2.

**Source:** `= this.source` (`= this.source-type`)
