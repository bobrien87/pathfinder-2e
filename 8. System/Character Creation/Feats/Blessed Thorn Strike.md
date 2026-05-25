---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Rose Warden|Rose Warden]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Divine]]", "[[Flourish]]", "[[Sanctified]]"]
prerequisites: "Rose Warden Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You witnessed an enemy harm an ally with a Strike or spell last round.

When you see a foe hurt one of your allies, your righteous retribution causes your weapon to sprout holy thorns. Make a Strike against the triggering enemy. If you hit and deal damage, the target must also succeed at a [[Fortitude]] save saving throw against your class DC or spell DC, whichever is higher, or become [[Enfeebled]] 1 (or [[Enfeebled]] 2 on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
