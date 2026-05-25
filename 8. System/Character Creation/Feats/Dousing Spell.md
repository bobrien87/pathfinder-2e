---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Elementalist|Elementalist]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Spellshape]]", "[[Water]]"]
prerequisites: "Elementalist Dedication, water is in your elemental philosophy"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You enhance your spell with elemental water, soaking the target. If the next action you use is to Cast a Spell targeting a single creature, you soak the target of the spell with water. If the target has [[Persistent Acid or Fire Damage]], the DC to end those conditions is reduced to 10, and the creature can attempt a flat check to end those types of persistent damage immediately. The spell gains the water trait (causing it to deal extra damage to creatures with weakness to water).

**Source:** `= this.source` (`= this.source-type`)
