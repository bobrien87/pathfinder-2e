---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Avenging Runelord|Avenging Runelord]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Avenging Runelord Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Magical markings of every kind seem eager to aid your endeavors. Whenever you read text, be it mundane or magical, the writing itself seems to almost to leap into your thoughts. You gain a +2 status bonus to checks to Decipher Writing, Identify Magic, Learn a Spell, or any Research check or [[Recall Knowledge]] check involving reading.

You gain a +2 status bonus to saving throws and to your AC against effects from hazards that involve reading, such as those created by a rune trap ritual. If you were the one who triggered the hazard by reading the triggering runes, the status bonus increases to +4.

If you prepare spells from a spellbook, you gain the [[Draw From the Pages]] activity.

**Source:** `= this.source` (`= this.source-type`)
