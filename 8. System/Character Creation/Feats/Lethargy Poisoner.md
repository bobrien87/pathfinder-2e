---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Crossbow Infiltrator|Crossbow Infiltrator]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Crossbow Infiltrator Dedication, trained in Crafting"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've learned more than the use of hand crossbows. During your daily preparations, you can prepare a dose of [[Lethargy Poison]] from ordinary materials in a wilderness or urban area. If you're an expert in Crafting, you can instead craft a dose of [[Stupor Poison]]. You can prepare two doses (of either poison) if you're a master in Crafting and three doses if you're legendary in Crafting. The save DC for this poison is equal to your class DC. Only you can use these poisons, and they expire the next time you make your daily preparations. The GM might decide that the area you're in is too barren to provide the materials you need for this feat.

**Source:** `= this.source` (`= this.source-type`)
