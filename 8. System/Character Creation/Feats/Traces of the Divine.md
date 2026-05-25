---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pure Legion Enforcer|Pure Legion Enforcer]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Exploration]]"]
prerequisites: "Pure Legion Enforcer Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can detect those who use divine magic like an additional sense. You gain a +2 circumstance bonus to Perception checks to `act seek` and Survival checks to `act track` creatures that can cast divine spells. In addition, you automatically succeed at the flat check to target a [[Concealed]] creature that can cast divine spells, and the flat check to target a hidden creature that can cast divine spells is reduced to DC 5.

**Source:** `= this.source` (`= this.source-type`)
