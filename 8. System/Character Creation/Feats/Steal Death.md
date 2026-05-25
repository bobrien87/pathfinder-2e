---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Apocalypse Rider|Apocalypse Rider]]"
source-type: "Remaster"
level: "16"
traits: ["[[Death]]", "[[Mythic]]"]
prerequisites: "Apocalypse Rider Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** Another creature within 30 feet gains the [[Doomed]] or [[Dying]] condition or their doomed or dying condition increases.

As a harbinger of daemonkind, you gain authority to delay the death of others if it serves your purposes, and in doing so, you bolster the well-being of both you and your mount to allow you sow further havoc. The triggering creature reduces their doomed or dying condition by 1.

For the next minute, you and your apocalypse mount gain fast healing 5 as long as you are within 10 feet of each other. If you use this reaction again within that minute, you and your mount's fast healing increases by 1, but the duration isn't increased.

> [!danger] Effect: Steal Death

**Source:** `= this.source` (`= this.source-type`)
