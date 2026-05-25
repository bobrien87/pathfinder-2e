---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Amp]]", "[[Emotion]]", "[[Mental]]", "[[Psychic]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your spells release soothing mental waves. Use this amp in place of a psi cantrip's normal amp entry. You can use this amp only on a psi cantrip that targets or affects you or one or more of your allies and doesn't target or affect any enemies.

**Amp** You or one ally within 30 feet gains a +2 status bonus to Will saves against emotion effects for 1 minute. You can also have the amped psi cantrip attempt to counteract one effect imposing the frightened condition on yourself or the chosen ally, or an effect imposing the stupefied condition that has a duration of 1 hour or less. If you successfully counteract the effect, you remove only the frightened and stupefied conditions, not any other part of the effect.

**Source:** `= this.source` (`= this.source-type`)
