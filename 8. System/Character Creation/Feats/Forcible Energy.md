---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Manipulate]]", "[[Spellshape]]", "[[Wizard]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You perform complex manipulations to make the energy from your spells so powerful that your enemies remain vulnerable to it afterward. If your next action is to Cast a Spell that deals acid, cold, electricity, fire, or sonic damage, you can select one target that was damaged to gain weakness 5 to that damage type until the end of your next turn. If a spell deals multiple types of energy damage, choose one that the target gains weakness to. This has no effect on creatures with resistance or immunity to the energy type you choose.

> [!danger] Effect: Forcible Energy

**Source:** `= this.source` (`= this.source-type`)
