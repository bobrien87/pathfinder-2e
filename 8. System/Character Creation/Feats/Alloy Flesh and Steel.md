---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Manipulate]]", "[[Metal]]", "[[Polymorph]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Elemental energy replaces every cell of your body with raw metal. You gain the benefits of the [[Ferrous Form]] spell (except you can't cast *needle darts*) until the end of your next turn. You can Sustain the impulse up to 1 minute, and when you do, you can Raise a metal Shield if you're wielding one. Your metal Elemental Blasts deal an additional die of damage. If you suspend any conditions with Alloy Flesh and Steel, when it ends, you're temporarily immune to Alloy Flesh and Steel for 1 hour.

**Level (16th)** The resistance is 15.

**Source:** `= this.source` (`= this.source-type`)
