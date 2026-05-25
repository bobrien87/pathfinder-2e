---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Monk]]"]
prerequisites: "at least two stances"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have combined two stances into a single stance all your own. When you take this feat, choose two stances you know and combine them into a single fused stance. Give your new fused stance a unique name. When you enter your fused stance, you gain all the effects of both stances, including the requirements and restrictions.

If the stances both grant special attacks, you gain all those attacks. If a stance restricts you to one particular attack (such as Crane Stance), you must abide by that restriction. If the fused stances have incompatible restrictions, the GM determines which apply, or determines you can't fuse those stances at all.

**Source:** `= this.source` (`= this.source-type`)
