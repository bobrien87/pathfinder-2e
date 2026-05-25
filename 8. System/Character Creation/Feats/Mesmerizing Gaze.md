---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Celebrity|Celebrity]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Emotion]]", "[[Mental]]", "[[Visual]]"]
prerequisites: "Celebrity Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you meet someone's gaze, they're unable to look away from you. Choose one target creature you can see and that can see you. That creature must succeed at a [[Will]] save or be [[Fascinated]] with you until the end of your next turn; the DC is the higher of your class DC or spell DC. If the creature succeeds at its save or its fascination ends due to a hostile action, it becomes temporarily immune to your Mesmerizing Gaze for 1 day.

**Source:** `= this.source` (`= this.source-type`)
