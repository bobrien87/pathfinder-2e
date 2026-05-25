---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Arcane]]", "[[Sorcerer]]"]
prerequisites: "bloodline that grants arcane spells"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your arcane legacy allows you to perceive how magic affects everything. You become trained in one skill of your choice.

Additionally, you can use arcane arts to tinker with your selection of spells. During your daily preparations, you can choose one spell in your spell repertoire to be a signature spell that day.

You can use the [[Learn a Spell]] activity to add more arcane spells to the list you choose from, but if you prepare a spell that isn't in your repertoire, you temporarily add it to your repertoire at the spell rank of your choice instead of making it a signature spell.

**Source:** `= this.source` (`= this.source-type`)
