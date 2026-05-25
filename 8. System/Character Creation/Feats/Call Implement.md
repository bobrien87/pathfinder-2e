---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Arcane]]", "[[Manipulate]]", "[[Teleportation]]", "[[Thaumaturge]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a free hand.

You can tug on the bonds of ownership between yourself and your implement, causing it to find its way back to you. You look down and find that your implement has mysteriously appeared in your free hand, as long as the implement was within 1 mile and on the same plane of existence. If your implement is attended by another creature, that creature can prevent the implement from teleporting away if it succeeds at a [[Will]] save against your class DC. If the creature succeeds, you can't attempt to Call that Implement again until midnight.

**Source:** `= this.source` (`= this.source-type`)
