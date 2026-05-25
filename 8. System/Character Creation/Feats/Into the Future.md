---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Time Mage|Time Mage]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Spellshape]]"]
prerequisites: "Time Mage Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know your spell will be needed not now but in a few moments, so you cast your magic into the future. If your next action is to Cast a Spell that takes 1 or 2 actions to cast, the spell's effects occur 1 round later, at the beginning of your next turn, rather than immediately. Targets and choices about the spell must be determined when the spell is cast, and requirements, such as line of sight and line of effect, must be valid both when the spell is cast and when its effects occur. Consequences for the action of Casting the Spell itself, such as a Reactive Strike reaction or ending a foe's [[Fascinated]] condition by taking a hostile action, aren't delayed.

**Source:** `= this.source` (`= this.source-type`)
