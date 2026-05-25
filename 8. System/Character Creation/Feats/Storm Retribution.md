---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Druid]]"]
prerequisites: "storm order, tempest surge order spell"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An opponent adjacent to you critically hits you with a melee weapon or melee unarmed attack.

**Requirements** You have at least 1 available Focus Point.

You lash out, directing a burst of storming fury toward a creature that has harmed you. You cast [[Tempest Surge]] on the triggering opponent and push that creature, moving it 5 feet away from you if it fails its Reflex save, or 10 feet if it critically fails. This movement is forced movement.

**Source:** `= this.source` (`= this.source-type`)
