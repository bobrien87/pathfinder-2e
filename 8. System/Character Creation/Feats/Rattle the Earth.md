---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Striking the ground with the gravity of the deepest rocks, you cause an earthquake. This has the effects of [[Earthquake]] but comes from you, with an area of a @Template[cone|distance:60] or an emanation with the same size as your kinetic aura. You and your space are unaffected by the quake. The fissures are only 10 feet deep, and the DC of the flat check for a collapse is 4 higher.

**Level (16th)** Fissures are 20 feet deep, and the DC of the flat check is 2 higher.

**Level (20th)** The fissures and flat check are unchanged from the spell.

**Source:** `= this.source` (`= this.source-type`)
