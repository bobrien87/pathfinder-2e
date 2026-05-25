---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Nidalese Horselord|Nidalese Horselord]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Occult]]", "[[Sanctified]]"]
prerequisites: "Nidalese Horselord Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A fiend within 15 feet of you damages you with a Strike.

You turn to face a fiend that attacked you, looking them squarely in the eyes (if it has them) and showing no fear. You increase the amount of damage you take by @Damage[(ternary(gte(@actor.level,18),5,4))d6], and deal @Damage[(ternary(gte(@actor.level,18),5,4))d6[spirit]] damage to the triggering fiend. The damage you take and deal increases to 5d6 at 18th level.

In addition, if the fiend has an aura and you're in it, you can attempt an [[Intimidation]] check to counteract the aura's effect, using half your level rounded up as the counteract rank. If you succeed, the effects of the aura are suppressed until the end of the triggering fiend's next turn.

**Source:** `= this.source` (`= this.source-type`)
