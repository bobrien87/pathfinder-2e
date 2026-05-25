---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Prophet Of Kalistrade|Prophet Of Kalistrade]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Prophet of Kalistrade Dedication"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Kalistrade teaches that setbacks are only temporary and that perseverance is a treasured virtue. When you fail, but not critically fail, at a Society or Mercantile Lore check to [[Earn Income]] at a specific task and are allowed to continue working at that task on subsequent days, you can choose to attempt the skill check again the next day. If you succeed, you get a critical success and continue to earn that amount on further days spent working at the task, if the task lasts that long.

**Source:** `= this.source` (`= this.source-type`)
