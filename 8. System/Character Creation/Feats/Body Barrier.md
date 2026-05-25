---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Knight Vigilant|Knight Vigilant]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]"]
prerequisites: "Knight Vigilant Dedication"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You and at least one ally are in the area of an effect that requires a Reflex save.

When your allies are in danger, you don't hesitate to take the brunt of the blow for them. You grant all allies in the area standard cover against the triggering effect, and you gain weakness to all damage against the triggering effect equal to twice the number of allies that gain cover in this way.

**Source:** `= this.source` (`= this.source-type`)
