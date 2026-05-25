---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Witch]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have prepared a special knife to direct energies when spellcasting. During your daily preparations, you and your familiar can perform a short ritual over a weapon in the knife group—typically a dagger. This causes the knife to function as a magic wand, containing any one 1st-rank spell your familiar knows. You, and only you, can Activate the knife to Cast the Spell within it, as normal for a wand. You can attempt to overcharge the knife, and this can break or destroy the knife as normal. You can have only one ceremonial knife at a time.

At 8th level, and every 2 levels thereafter, the maximum rank of spell your ceremonial knife can hold increases by 1.

**Source:** `= this.source` (`= this.source-type`)
