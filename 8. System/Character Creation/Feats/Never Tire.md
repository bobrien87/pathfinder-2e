---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Celebrity|Celebrity]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Celebrity Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You would gain the [[Fatigued]] condition.

**Requirements** You are [[Observed]] by at least three creatures who aren't enemies.

As long as you have an audience, you can continue to perform even when you are on the brink of collapse. Indeed, you must—you have an obligation to your fans! You delay the effects of the [[Fatigued]] condition for 1 minute or until you are no longer observed by at least three creatures who aren't enemies, whichever comes first. If the fatigued condition has a duration, the duration begins to elapse only after the delay. You can't further delay or prevent the fatigued condition after this ability ends.

**Source:** `= this.source` (`= this.source-type`)
