---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Manipulate]]", "[[Rogue]]"]
frequency: "once per day"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a weapon.

You apply a contact poison or injury poison to the required weapon; if you have a free hand, you can Interact to draw a poison as part of this action. This poison can be one of the simple injury poisons you can create due to this feat, or another contact or injury poison you've acquired.

**Special** During your daily preparations, you can prepare a number of simple injury poisons equal to your level. These follow the rules for injury poisons, except that they deal 1d4 poison damage with no saving throw. Only you can apply these poisons properly, and they expire the next time you prepare.

**Source:** `= this.source` (`= this.source-type`)
