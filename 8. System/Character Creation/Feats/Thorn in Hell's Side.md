---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellbreaker|Hellbreaker]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Defy Hell"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your devotion to the ideals of justice, freedom, and revolution allow you to truly punish those who stand in your way. When you critically succeed at a Hellbreaker Strike, the target must succeed at a [[Fortitude]] save against your class DC or spell DC, whichever is higher, or become [[Stunned]] 1 ([[Stunned]] 2 on a critical failure). This effect has the incapacitation trait.

**Source:** `= this.source` (`= this.source-type`)
