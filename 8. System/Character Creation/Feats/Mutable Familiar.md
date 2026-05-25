---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Familiar Master|Familiar Master]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Familiar Master Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your familiar's supernatural spirit has outgrown its corporeal body. You can conduct a special 10-minute activity to reselect certain familiar abilities, switching one or more of the following abilities for other abilities on this list: amphibious, burrower, climber, darkvision, fast movement, manual dexterity, resistance, and scent.

You can reselect only familiar abilities you would normally be able to reselect each day, not required familiar abilities for your familiar. You can't remove an ability that is required for another ability your familiar has (for instance, you can't remove manual dexterity if the familiar has lab assistant).

**Source:** `= this.source` (`= this.source-type`)
