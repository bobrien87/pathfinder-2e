---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Time Mage|Time Mage]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Spellshape]]"]
prerequisites: "Time Mage Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Rather than conjuring creatures from elsewhere in the world or the planes, you can temporarily pull a much different version of yourself from an alternate timeline—for instance, instead of summoning a generic or random troll with [[Summon Giant]], you summon a troll version of yourself from a timeline where you're a troll. If your next action is to Cast a Spell that summons a creature, that creature is another version of you. This creature remains the type of creature you summoned and has largely the same abilities (plus the following adjustments), but it clearly resembles you, likely sharing some distinguishing features, such as mannerisms, speech patterns, tattoos, or clothing. The summoned creature gains a +1 status bonus to any skill check in which you're trained, a +2 status bonus if you're an expert, a +3 status bonus if you're a master, or a +4 status bonus if you're legendary. The creature also takes a –2 penalty to all skills in which you're untrained.

**Source:** `= this.source` (`= this.source-type`)
