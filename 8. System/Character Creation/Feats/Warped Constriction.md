---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Living Vessel|Living Vessel]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Living Vessel Dedication, your entity is an aberration or outer entity"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have an enemy [[Grabbed]] or [[Restrained]].

The entity inhabiting your body is an aberrant being with unfathomable motivations, and when you hold a foe close, tendrils and tentacles unfurl from your body to crush your foe and pollute it with alien wrongness. Your grabbed or restrained foe takes bludgeoning damage equal to your level and mental damage equal to your highest mental attribute modifier. The creature attempts a basic Will save that applies to both types of damage and uses the higher of your class DC or spell DC.

**Source:** `= this.source` (`= this.source-type`)
