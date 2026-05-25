---
type: action
source-type: "Remaster"
cast: "`pf2:2`"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per round

**Effect** Each enemy in your aura takes @Damage[ternary(gte(@actor.level, 18), 7, ternary(gte(@actor.level, 15), 6, 5))d6[acid]] damage and 2d6 persistent,acid damage with a [[Reflex]] save against your class DC or spell DC, whichever is higher. The initial damage increases to 6d6 at 15th level and 7d6 at 18th level.

**Source:** `= this.source` (`= this.source-type`)
