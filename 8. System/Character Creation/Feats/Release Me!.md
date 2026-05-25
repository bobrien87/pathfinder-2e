---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Broken Chain|Broken Chain]]"
source-type: "Remaster"
level: "14"
traits: ["[[Flourish]]", "[[Mythic]]"]
prerequisites: "Broken Chain Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** An enemy has you [[Grabbed]] or [[Restrained]].

Your retribution against one who would detain you is swift and dangerous. Make a melee Strike against the creature who has you [[Grabbed]] or [[Restrained]]. You can still make this attack even if you are restrained, though not if you are wielding a two-handed weapon. Unless your Strike is a critical failure, you can then attempt a check to [[Escape]]. If the creature who has you grabbed or restrained is the target of your [[Ultimatum of Liberation]], you gain a +2 circumstance bonus to this check. Both the Strike and the Escape count toward your multiple attack penalty, but it doesn't increase until you've made both rolls.

**Source:** `= this.source` (`= this.source-type`)
