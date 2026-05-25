---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Elementalist|Elementalist]]"
source-type: "Remaster"
level: "14"
traits: ["[[Air]]", "[[Archetype]]", "[[Concentrate]]", "[[Spellshape]]"]
prerequisites: "Elementalist Dedication, air is in your elemental philosophy"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You enhance your spell with elemental air, using the wind to find your target and carry your magic around cover. If the next action you use is to Cast a Spell that requires a spell attack roll, you ignore the target's [[Concealed]] condition and any cover they have from you. The spell gains the air trait.

**Source:** `= this.source` (`= this.source-type`)
