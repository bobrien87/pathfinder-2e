---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pirate|Pirate]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Pirate Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're particularly skilled at wielding the weapons used traditionally by pirates. You gain either the [[Combat Climber]] or [[Underwater Marauder]] skill feat, even if you do not meet its prerequisites. You have familiarity with the following weapons: [[Hatchet]], [[Rapier]], [[Scimitar]], and [[Whip]]—for the purposes of proficiency, you treat any of these weapons as simple weapons. Your GM may add additional martial weapons to this list as appropriate for your world or region.

At 5th level, whenever you get a critical hit with one of these weapons, you get its critical specialization effect.

**Source:** `= this.source` (`= this.source-type`)
