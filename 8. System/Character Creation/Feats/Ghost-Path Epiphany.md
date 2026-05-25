---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Cultivator|Cultivator]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Cultivator Dedication, you aren't holy"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Deviating from the orthodox path, you tread an inauspicious descent littered with flowers of death; this heretical choice will, in time, earn you the enmity and fear of more traditional cultivators. You become sanctified with the unholy trait. You also learn the [[Call Spirit]] and [[Commune]] rituals, which can be used to contact only undead or entities from the Void or the Netherworld.

When you cast a ritual, you can reduce the number of secondary casters by 1 as you direct decaying fragments of your own soul, felled by your proximity to death, to assist with the ritual. When you do, you must fulfill any requirements for the secondary caster, and you attempt the secondary check normally performed by that secondary caster. You can't replace a secondary caster who's the target of the spell (as in the atone ritual).

**Source:** `= this.source` (`= this.source-type`)
