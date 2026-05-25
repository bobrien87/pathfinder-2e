---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Elementalist|Elementalist]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Fire]]", "[[Spellshape]]"]
prerequisites: "Elementalist Dedication, fire is in your elemental philosophy"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You enhance your spell with elemental fire, causing it to set the target on fire. If the next action you use is to Cast a non-cantrip Spell that deals damage at a single target, the spell deals additional [[Persistent Fire Damage]] equal to the spell rank, in addition to its other effects. This has no effect if the spell already deals persistent fire damage. The spell gains the fire trait.

**Source:** `= this.source` (`= this.source-type`)
