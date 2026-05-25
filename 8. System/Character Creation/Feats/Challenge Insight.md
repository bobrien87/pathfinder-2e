---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Palatine Detective|Palatine Detective]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Auditory]]"]
prerequisites: "Palatine Detective Dedication"
frequency: "once per day"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** A creature you can see Casts a Spell that is from the divine or occult tradition.

**Requirements** The triggering caster must be able to hear and understand you.

Your deep grasp of the mystical lets you know exactly what to say to make others doubt how well they understand the source of their own power.

Attempt a counteract check against the triggering spell. Your counteract rank is half your level rounded up. You use your Occultism modifier as your counteract modifier if the triggering spell is from the occult tradition, or your Religion modifier if the triggering spell is from the divine tradition.

If you successfully counteract the spell, the caster becomes [[Stupefied 1]] until the end of their next turn.

**Source:** `= this.source` (`= this.source-type`)
