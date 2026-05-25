---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Twilight Talon|Twilight Talon]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "expert in Deception"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You're invited by a current member of the Twilight Talons.

Few would even suspect that you're a member of the Eagle Knights, and you use the tricks of the spymaster's trade to keep it that way. You gain the [[Additional Lore]] general feat for Espionage Lore. If you were already trained in Espionage Lore, you also become trained in a Lore skill of your choice.

During your daily preparations, you can brush up on a specific field to gain the trained proficiency rank in one Lore skill of your choice. This proficiency lasts until you prepare again. Since this proficiency is temporary, you can't use it as a prerequisite for a skill increase or a permanent character option like a feat. If you have master proficiency in Espionage Lore, you gain expert proficiency in the chosen skill instead, and if you have legendary proficiency in Espionage Lore, you gain master proficiency in the skill.

**Special** You can take this dedication even if you haven't taken more than two non-dedication feats from the Eagle Knight archetype.

Twilight Talon

**Source:** `= this.source` (`= this.source-type`)
