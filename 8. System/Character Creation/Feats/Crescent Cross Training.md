---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Crossbow Infiltrator|Crossbow Infiltrator]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Crossbow Infiltrator Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have familiarity with the [[Crescent Cross]], an ingenious weapon that combines an arm-mounted, multi-chamber crossbow with a crescent-shaped blade. For the purposes of proficiency, you treat both its configurations as simple weapons.

Feats and abilities from this archetype that normally work with a gauntlet bow also work with your crescent cross, treating the melee form of the crescent cross as a gauntlet where appropriate. You gain the [[Crescent Spray]] action.

**Source:** `= this.source` (`= this.source-type`)
