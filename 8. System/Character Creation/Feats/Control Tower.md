---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Overwatch|Overwatch]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]"]
prerequisites: "Overwatch Dedication, master in Perception"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your keen senses and ability to process battlefield information have dramatically improved, allowing you to drastically reduce the advantage of unseen foes. You and allies in your overwatch field gain a +2 circumstance bonus when using the Seek action to find [[Hidden]] or [[Undetected]] creatures within the overwatch field.

> [!danger] Effect: Control Tower

You and your allies don't have to succeed at a flat check to target a concealed creature within your overwatch field. When you or an ally targets a hidden creature in your overwatch field, reduce the DC of the flat check to 5.

**Source:** `= this.source` (`= this.source-type`)
