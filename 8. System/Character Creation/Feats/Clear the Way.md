---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mauler|Mauler]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Mauler Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a melee weapon in two hands.

You put your body behind your massive weapon and swing, shoving enemies to clear a wide path. You attempt to [[Shove]] up to five creatures adjacent to you, rolling a separate Athletics check for each target and ignoring the requirement that you have a hand free. Then Stride up to half your Speed. This movement doesn't trigger reactions from any of the creatures you successfully Shoved. Each attack counts toward your multiple attack penalty, but don't increase your penalty until you have made all your attacks.

**Source:** `= this.source` (`= this.source-type`)
