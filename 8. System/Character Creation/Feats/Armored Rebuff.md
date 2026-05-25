---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sentinel|Sentinel]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Sentinel Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An adjacent foe critically fails an attack roll to Strike you with a melee weapon or unarmed attack.

**Requirements** You are wearing medium armor or heavier.

You rebuff puny attacks with your armor, knocking back your foe. Attempt an Athletics check to [[Shove]] the triggering foe, even if you don't have a hand free. If you succeed, you can't Stride to follow the foe, as you're knocking the foe back with the rebounded attack, not by physically moving towards them.

**Source:** `= this.source` (`= this.source-type`)
