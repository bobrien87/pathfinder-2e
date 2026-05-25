---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Guerrilla|Guerrilla]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]"]
prerequisites: "Guerrilla Dedication, Poisoned Sticks and Stones"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your carefully prepared and placed shot brings instant death to your target. Attempt a Strike with a blowgun or sling using ammunition that you have poisoned with your simple injury poison. If the Strike is successful and you are [[Hidden]] from the target, or unnoticed or undetected by them, the target must succeed at a [[Fortitude]] save against your class DC or die; this is a death and incapacitation effect. A creature that survives is temporarily immune to the instant death effect of Deathblow for 1 day.

**Source:** `= this.source` (`= this.source-type`)
