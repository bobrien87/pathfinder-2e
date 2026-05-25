---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 450}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell

This catalyst is made from twisted sapling bark harvested under a full moon. When used to cast a [[Charm]] spell, the spell creates a blissful experience for all targets of the spell. When the spell ends, even if you Dismiss it, the sudden mental dissonance between the charmed state and reality forces all targets of the *charm* spell to attempt a Will save against your spell DC.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Stunned]] 1 or, if the spell ended because of a hostile action, [[Confused]] for 1 round.
- **Failure** The target is [[Stunned]] 2 or, if the spell ended because of a hostile action, confused for 1 round.
- **Critical Failure** The target is [[Stunned]] 3 or, if the spell ended because of a hostile action, confused for 2 rounds.

**Source:** `= this.source` (`= this.source-type`)
