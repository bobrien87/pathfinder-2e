---
type: action
source-type: "Remaster"
traits: ["[[Fire]]", "[[Sonic]]", "[[Visual]]"]
cast: "`pf2:3`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Chaos fills a @Template[burst|distance:20] within 120 feet. All creatures in the area takes @Damage[(max(3,(3 + floor((@actor.level - 10)/ 3))))d6[fire],(max(3,(3 + floor((@actor.level - 10)/ 3))))d6[sonic]|options:area-damage] damage and must attempt a [[Fortitude]] save. Every 3 levels, the fire damage and sonic damage each increase by 1d6. You can expend 2 versatile vials instead of 1 to increase the fire and sonic damage by 1d6 each, or by 2d6 each at 16th level.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Dazzled]] and [[Deafened]] until the end of its next turn and takes half damage.
- **Failure** The creature is dazzled and deafened for 1 minute and takes full damage.
- **Critical Failure** The creature is [[Blinded]] for 1 round, dazzled and deafened for 1 minute, and takes double damage.

**Source:** `= this.source` (`= this.source-type`)
