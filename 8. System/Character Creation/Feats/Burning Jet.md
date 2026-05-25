---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A condensed burst of flame shoots behind you, propelling you forward with its sheer force. Stride up to 40 feet in a straight line. Movement from this impulse ignores difficult terrain and doesn't trigger reactions.

**Level (6th)** The maximum distance of the Stride is 60 feet. You can choose to [[Leap]] up to 40 feet in any direction instead of Striding. If you're in the air at the end of this Leap, you fall normally.

**Level (10th)** As 6th level, but you hover briefly after leaping into the air. If you Leap, you don't fall until the end of your next turn. If you use Burning Jet again on a subsequent turn, you remain airborne.

**Source:** `= this.source` (`= this.source-type`)
