---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Bard]]", "[[Concentrate]]", "[[Oracle]]", "[[Sorcerer]]", "[[Spellshape]]", "[[Witch]]", "[[Wizard]]"]
frequency: "once per day"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Bard** If your next action is to cast a bard cantrip or a bard spell that is at least 2 ranks lower than the highest-rank bard spell slot you have, reduce the number of actions to cast it by 1 (minimum 1 action).

**Witch** You accelerate your spellcasting. If your next action is to cast a witch cantrip or a witch spell that is at least 2 ranks lower than the highest-rank witch spell slot you have, reduce the number of actions to cast it by 1 (minimum 1 action).

**Wizard** Straining your mind, you collapse as much of your spell's formulas as you can, resulting in a shorter but much more complex incantation. If your next action is to cast a wizard cantrip or a wizard spell that is at least 2 ranks lower than the highest-rank wizard spell slot you have, reduce the number of actions to cast it by 1 (minimum 1 action).

**Others** If your next action is to cast a class cantrip or a class spell that is at least 2 levels lower than the highest-level class spell slot you have, reduce the number of actions to cast it by 1 (minimum 1 action).

**Source:** `= this.source` (`= this.source-type`)
