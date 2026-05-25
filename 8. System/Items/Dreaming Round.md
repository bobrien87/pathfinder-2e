---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Incapacitation]]", "[[Magical]]", "[[Mental]]", "[[Sleep]]"]
price: "{'gp': 900}"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** round

**Activate** `pf2:1` (concentrate)

The night sky seems contained in this glass projectile. When an activated *dreaming round* damages a creature, it induces drowsiness. The creature must attempt a DC 30 [[Fortitude]] save.
- **Critical Success** The creature is unaffected and becomes temporarily immune for 1 minute.
- **Success** The creature becomes [[Slowed]] 1 and [[Fatigued]] for 1 round.
- **Failure** The creature becomes fatigued and slowed 1, and must attempt another Fortitude save at the end of each of its turns. If it fails, its slowed condition increases by 1. A successful save reduces the slowed condition by 1. If the slowed condition is removed or reduced to 0, the effect and the fatigued condition end. If the target's actions are reduced to 0 by this effect, it immediately falls into a deep sleep and is [[Unconscious]], during which it no longer attempts a save at the end of its turn. It wakes up automatically after 1 hour or if it takes damage, but not due to non-painful stimuli (such as noise or being nudged). When it wakes up, its slowed condition decreases by 1, though it must once again save at the end of each of its turns and might risk falling asleep again.
- **Critical Failure** As failure, except the target is initially [[Slowed]] 2.

**Source:** `= this.source` (`= this.source-type`)
