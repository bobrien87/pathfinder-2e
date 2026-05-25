---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 70, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

These iron rings filled with kaleidoscopic glass are popular among Shelynites. A *chroma kaleidoscope*'s effects last for 1 hour. When you critically Strike a creature with a weapon under the effects of a *chroma kaleidoscope*, a blast of color from the weapon forces them to attempt a [[Will]] save saving throw against your class DC or spell DC, whichever is higher, with the following effects.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Dazzled]] for 1 round.
- **Failure** The creature is [[Blinded]] for 1 round and dazzled for 1 round after the blindness ends.
- **Critical Failure** The creature is [[Stunned]] 1 and blinded for 1 round, and dazzled for 1 round after the blindness ends.

**Source:** `= this.source` (`= this.source-type`)
