---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Blackjacket|Blackjacket]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Auditory]]"]
prerequisites: "Blackjacket Dedication"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An ally within 30 feet of you critically fails a Strike.

You can recognize when a strategy isn't working and advise your ally to change course. The next Strike the triggering ally makes before the end of their turn has the same multiple attack penalty as the critically failed Strike, but it counts toward their multiple attack penalty as normal.

**Source:** `= this.source` (`= this.source-type`)
