---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** An enemy attempts a skill check and doesn't get a critical success

After your foe has tried their best, you show everyone how it's really done. Attempt a check using the same skill that triggered this reaction.
- **Critical Success** You gain a +1 status bonus to attack rolls, Perception checks, saving throws, and skill checks until the end of your next turn.
- **Success** As critical success, except you gain the benefits only if the triggering creature failed their skill check.

> [!danger] Effect: Upstage

**Source:** `= this.source` (`= this.source-type`)
