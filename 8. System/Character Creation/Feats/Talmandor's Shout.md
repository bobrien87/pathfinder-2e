---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eagle Knight|Eagle Knight]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Eagle Knight Dedication, master in Intimidation"
frequency: "once per day"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Requirements** You witnessed a creature deal damage to an ally within 30 feet since your last turn.

After seeing an enemy harm one of your allies, you deliver a righteous shout in the name of the celestial Talmandor. Attempt an Intimidation check to [[Demoralize]], comparing the result to the Will DC of each enemy within a @Template[type:emanation|distance:60]; this Demoralize attempt doesn't take any penalty for not sharing a language. It's possible to get a different degree of success for each target.

**Source:** `= this.source` (`= this.source-type`)
