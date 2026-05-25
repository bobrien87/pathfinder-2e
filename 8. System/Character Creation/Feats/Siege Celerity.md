---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Munitions Master|Munitions Master]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Manipulate]]", "[[Unstable]]"]
prerequisites: "Munitions Master Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** Your turn begins.

You push yourself and your light mortar beyond your limits. You are [[Quickened]] for this turn. You can use the extra action to Load or Launch your light mortar. This doesn't allow you bypass the normal limit of one Launch per round.

**Source:** `= this.source` (`= this.source-type`)
