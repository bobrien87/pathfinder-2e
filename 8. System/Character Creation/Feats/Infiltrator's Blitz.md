---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Crossbow Infiltrator|Crossbow Infiltrator]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]"]
prerequisites: "Crossbow Infiltrator Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're not [[Fatigued]].

Though your training is meant to ensure you don't get caught by your enemies, your missions are often high risk, and sometimes the only option you have left when things go wrong is to unleash a blistering torrent of violence while running away as fast as possible.

You can attempt to [[Escape]] any effect that is currently immobilizing you. You gain a +10-foot circumstance bonus to your Speed and can Stride up to three times. At any point during each of these Strides, you can Strike with a weapon you have familiarity with from this archetype and can then immediately Interact to reload that weapon.

After using Infiltrator's Blitz, you become fatigued for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
