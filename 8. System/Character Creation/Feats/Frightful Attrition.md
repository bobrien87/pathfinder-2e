---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Guerrilla|Guerrilla]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Emotion]]", "[[Fear]]", "[[Incapacitation]]", "[[Mental]]"]
prerequisites: "Guerrilla Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your diminishment of your foes' ranks damages their morale. Whenever you reduce a creature to 0 HP with a Strike or spell, all enemies within 30 feet of the downed creature who witnessed the attack must attempt a [[Will]] save saving throw against your class DC. A creature that didn't see you directly (such as if you're [[Invisible]] or remained [[Hidden]] after the attack) takes a –2 circumstance penalty to this save. Regardless of the result, each creature is temporarily immune to your Frightful Attrition for 10 minutes.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Frightened]] 1.
- **Failure** The creature is [[Frightened]] 2.
- **Critical Failure** The creature is [[Frightened]] 3 and [[Fleeing]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
