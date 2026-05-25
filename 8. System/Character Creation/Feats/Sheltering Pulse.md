---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Spirit Warrior|Spirit Warrior]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Manipulate]]"]
prerequisites: "Spirit Warrior Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You thrust your hand or weapon into the ground and release a pulse that creates a sheltering nexus of energy for you and your allies. Choose an unoccupied square within 15 feet. The nexus appears in a @Template[type:emanation|distance:15] around that square and lasts for 3 rounds. You and your allies gain a +1 status bonus to AC while in the area.

> [!danger] Effect: Sheltering Pulse

**Source:** `= this.source` (`= this.source-type`)
