---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Manipulate]]", "[[Spellshape]]", "[[Wizard]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You divert some of your spell's energy into an unstable runic array. If your next action is to Cast a Spell that deals damage, has no duration, and affects an area, a glowing magic circle appears in a @Template[burst|distance:5] within that area. At the beginning of your next turn, the circle detonates, dealing 1d6 force damage per rank of the spell to all creatures within the circle, with a basic Reflex save against your spell DC. If the spell dealt a different type of damage, the circle deals this type of damage instead (or one type of your choice if the spell could deal multiple types of damage).

**Source:** `= this.source` (`= this.source-type`)
