---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Lepidstadt Surgeon|Lepidstadt Surgeon]]"
source-type: "Remaster"
level: "7"
traits: ["[[Archetype]]", "[[Exploration]]", "[[Manipulate]]", "[[Skill]]"]
prerequisites: "Lepidstadt Surgeon Dedication, master in Medicine"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You perform surgical adjustments to disguise a willing ally or your construct companion. This counts as preparing a disguise to Impersonate, taking 10 minutes and requiring a healer's toolkit instead of a disguise kit. The DC to see through the deception with [[Seek]] is your Medicine DC ([[Perception]] check) unless the disguised character's Deception DC is higher. If the target directly interacts with someone while disguised, they gain a +2 circumstance bonus to their Deception check.

You can reverse this effect with another 10-minute surgery. The disguised character can also end it as a free action when they receive any healing effect.

**Source:** `= this.source` (`= this.source-type`)
