---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Tripkee]]"]
prerequisites: "You are not immune to diseases or poisons"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You attempt a saving throw against a disease or poison effect that affects an area.

Your skin readily absorbs poison and can consciously draw toxins into your body to spare others. Attempt a counteract check against the triggering effect; your counteract rank equals half your level (rounded up), and for the roll use either your class DC – 10 or your spellcasting attribute modifier plus your spellcasting proficiency bonus. If you counteract the triggering effect, you end the effect for all other creatures in the area; however, you must still save against the effect with a –2 penalty to the initial save.

**Source:** `= this.source` (`= this.source-type`)
