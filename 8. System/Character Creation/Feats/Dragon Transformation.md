---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Barbarian]]", "[[Concentrate]]", "[[Polymorph]]", "[[Primal]]", "[[Rage]]"]
prerequisites: "Dragon's Rage Wings"
frequency: "once per PT10M"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You transform into a ferocious Large dragon, gaining the effects of 6th-rank [[Dragon Form]] except that you use your own AC and attack modifier, you apply your extra damage from [[Rage]], and the Dragon Breath action uses your class DC. Add the temporary Hit Points from dragon form to any you already have from entering a rage (or any other action with the rage trait). The action to Dismiss the transformation gains the rage trait.

At 18th level, you gain a +20-foot status bonus to your fly Speed, your damage bonus with dragon Strikes increases to +12, and you gain a +14 status bonus to your Dragon Breath damage.

**Source:** `= this.source` (`= this.source-type`)
