---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Halfling]]"]
prerequisites: "Step Lively"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You dart under the legs of your enemies in combat. You can end a successful [[Tumble Through]] action in a Large or larger enemy's space. Also, when using the Step Lively feat, you can Step into the triggering enemy's space. The enemy must have limbs or otherwise leave you enough room for this maneuver, as determined by the GM. For instance, you could share space with a giant or dragon, but not an ooze.

**Source:** `= this.source` (`= this.source-type`)
