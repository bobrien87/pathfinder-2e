---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wrestler|Wrestler]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Wrestler Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a creature [[Grabbed]] or [[Restrained]].

Your iron grip saps your opponent's strength. Attempt an Athletics check to `act grapple` the creature you have grabbed or restrained, with the following additional effects if you succeed.
- **Critical Success** The target is [[Enfeebled]] 2 until the end of its next turn and [[Enfeebled]] 1 for 1 minute.
- **Success** The target is enfeebled 1 until the end of its next turn.

**Source:** `= this.source` (`= this.source-type`)
