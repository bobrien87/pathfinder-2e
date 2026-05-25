---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Leshy]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can extend a tangle of vines or tendrils to support your arms and extend your reach. When you wield a melee weapon that requires two hands, doesn't have reach, and deals at least 1d6 damage, you can change between a typical two-handed grip and an extended two-handed grasp using an Interact action. Weapons wielded in your extended grasp gain reach of 10 feet. This grasp is less stable and powerful than a typical grip, reducing the weapon's damage die by 1 step.

**Source:** `= this.source` (`= this.source-type`)
