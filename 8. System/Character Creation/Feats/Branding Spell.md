---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellknight|Hellknight]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Curse]]", "[[Spellshape]]"]
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The flames of your magic mark a target as an enemy of order. If your next action is to Cast a non-cantrip Spell that deals fire damage, that spell brands the target with a mark only you can see if it fails its saving throw. This brand lasts for 1 week. For as long as the target is branded, you always know the general direction and approximate distance of the target's current location, as long as it's on the same plane. You also know the direction the branded target is currently moving, if any, as well as any conditions affecting it. You can have only one brand active at a time.

**Source:** `= this.source` (`= this.source-type`)
