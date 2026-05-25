---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Witch]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can brew magic in your cauldron, creating useful magical concoctions. You can use the Craft activity to create oils and potions. You immediately gain the formulas for four common 1st-level oils or potions. At 4th level and every 2 levels beyond that, you gain the formula for a common oil or potion of that level or lower (a 4th-level potion if you're 4th level, a 6th-level potion if you're 6th level, and so on). If you have a familiar, you can have your familiar learn these formulas rather than storing them in a formula book. Your familiar can learn new formulas in the same way it learns new spells, and these formulas are transferred from a slain familiar to a new familiar in the same way spells are.

During your daily preparations, you can create one temporary oil or potion using a formula you know. If you have master proficiency in spell DC, you can create a batch of two temporary oils or potions during your daily preparations, and if you have legendary proficiency, you can create a batch of three. Any items you create this way become inert bottles of liquid the next time you make your daily preparations, and any remaining effects of the temporary items end. A temporary oil or potion has no value.

**Source:** `= this.source` (`= this.source-type`)
