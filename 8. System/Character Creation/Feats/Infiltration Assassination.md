---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Crossbow Infiltrator|Crossbow Infiltrator]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Crossbow Infiltrator Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wearing a loaded gauntlet bow.

With a high-priority target in reach, you quickly move to eliminate them. Make a melee Strike using your gauntlet bow as a gauntlet. If the Strike is successful, you automatically latch onto the target, giving them the [[Grabbed]] condition, then make a ranged Strike against them with your gauntlet bow. This Strike does not trigger reactions normally triggered by ranged attacks. If you are holding or wearing an injury poison, you can apply it to the bolt used in the attack as a free action before making the ranged Strike.

**Source:** `= this.source` (`= this.source-type`)
