---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Kineticist|Kineticist]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]", "[[Multiclass]]"]
prerequisites: "Constitution +2"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You become trained in kineticist class DC and impulse attack rolls. Choose one element to be your kinetic element (air, earth, fire, metal, water, or wood). You gain a kinetic aura and the [[Channel Elements]] action, though you don't get to use an [[Elemental Blast]] or stance impulse when you take that action. You gain the Elemental Blast action. Your Elemental Blast does not automatically gain additional damage dice every four levels, instead requiring you to take the [[Improved Elemental Blast]] feat. You become trained in Nature; if you were already trained in Nature, you instead become trained in another skill of your choice.

Kineticist

**Source:** `= this.source` (`= this.source-type`)
