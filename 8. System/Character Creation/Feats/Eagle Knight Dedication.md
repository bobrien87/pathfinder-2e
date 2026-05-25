---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eagle Knight|Eagle Knight]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Diplomacy and Society"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You're invited by a current member of the Eagle Knights or the People's Council.

Eagle Knights are the marshals and envoys of Andoran and are committed to keeping the peace. On the first round of combat, if you roll Diplomacy for initiative, creatures that haven't acted are [[Off Guard]] to you. You gain the [[Additional Lore]] skill feat for Politics Lore. If you were already trained in Politics Lore, you also become trained in a Lore skill of your choice. You can use Politics Lore to `act make-an-impression skill=politics-lore` on or make a `act request skill=politics-lore` of government officials (or similar figures) or to `act gather-information skill=politics-lore` about them. If you critically succeed at a check to [[Gather Information]] with Politics Lore, you know the information without having to spend any time gathering it.

Eagle Knight

**Source:** `= this.source` (`= this.source-type`)
