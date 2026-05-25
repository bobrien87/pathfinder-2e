---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Knight Reclaimant|Knight Reclaimant]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]"]
prerequisites: "Knight Reclaimant Dedication, master proficiency in a weapon"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Inspired by the sixth line of the Crimson Oath, when you oppose the enemies of Lastwall, you aim to excise the rot from the land itself. Make a Strike against an undead creature using a weapon with which you have master proficiency. On a success, in addition to the attack's other effects, the creature takes a –2 status penalty to the DC of any curses, diseases, or poisons it can inflict for 1 round. On a critical success, the undead creature takes the –2 status penalty for 1 round, then a –1 status penalty for an additional round.

**Source:** `= this.source` (`= this.source-type`)
