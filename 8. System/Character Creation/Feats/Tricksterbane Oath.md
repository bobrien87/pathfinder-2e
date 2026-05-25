---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Spirit Warrior|Spirit Warrior]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Spirit Warrior Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've sworn an oath to ferret out and destroy malevolent shapechangers who pose as mortals with evil intent. You gain a +4 circumstance bonus to Perception checks to detect a shapechanged creature's disguise, and a +2 circumstance bonus to attempts to Recall Knowledge about shapechangers. Whenever you use [[Overwhelming Combination]] against a shapechanged creature, you attempt to counteract one polymorph effect on that creature. The counteract rank is half your level rounded up, and the counteract check modifier is your Charisma modifier + your proficiency bonus with the weapon used to Strike as part of your Overwhelming Combination. You gain the following edict.

**Edict** You must reveal and slay evil or predatory shapechangers you discover or encounter, as long as you have a reasonable chance of success.

**Source:** `= this.source` (`= this.source-type`)
