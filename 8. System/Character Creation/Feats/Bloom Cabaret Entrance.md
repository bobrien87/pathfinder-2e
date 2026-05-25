---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Dandy|Dandy]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Incapacitation]]", "[[Mental]]", "[[Visual]]"]
prerequisites: "Dandy Dedication"
frequency: "once per day"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** You're about to roll initiative.

In socially exclusive venues like the Ivy District's Bloom Cabaret, you've learned how to make an entrance. This confidence doesn't betray you when you find yourself about to enter combat, allowing you to throw enemies temporarily off-balance. Once per day, you can choose to not roll initiative. Instead, you voluntarily go last. If more than one character uses this ability or another ability to go last, use the normal rules for resolving a tie: NPCs and monsters act before PCs, and within those groups, the creature can choose whichever order they want.

Enemies who can see you must attempt a [[Will]] save saving throw against your class DC or spell DC, whichever is higher. On a failure, the enemy is overcome with anticipation for what you'll do or say next and can't use reactions for 1 round.

In addition, during your first turn, you gain a +2 circumstance bonus to the first Deception, Diplomacy, or Intimidation check you attempt.

> [!danger] Effect: Bloom Cabaret Entrance

**Source:** `= this.source` (`= this.source-type`)
