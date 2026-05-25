---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Campfire Chronicler|Campfire Chronicler]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Divine]]"]
prerequisites: "Campfire Chronicler Dedication"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The blessings of Isthralei connect you to the thrum of the stories that underlie all settlements. When attempting a check to [[Recall Knowledge]] about a city you have visited, you gain a +2 circumstance bonus and can use an associated Lore skill (such as Nerosyan Lore) with your level as your proficiency bonus even if you're untrained.

**Source:** `= this.source` (`= this.source-type`)
