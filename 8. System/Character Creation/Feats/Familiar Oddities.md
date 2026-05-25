---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Curse Maelstrom|Curse Maelstrom]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Curse Maelstrom Dedication, trained in Occultism or Curse Lore"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Perhaps due to the curse within you, curses occasionally perceive you as an extension of themselves and readily reveal themselves to you. You gain a +2 circumstance bonus to checks to [[Identify Magic]] on a cursed item or a spell that has the curse trait.

**Source:** `= this.source` (`= this.source-type`)
