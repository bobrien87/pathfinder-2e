---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Inventor]]"]
prerequisites: "Shared Overdrive"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You prepare a variety of incredible gizmos on each of your allies, linking them together through careful modification to enable you to power them up all at once. During your daily preparations, select up to six willing allies. Whenever you Overdrive, you grant the benefits of your overdrive to any of these allies you choose who are within 30 feet of you. The allies don't gain the increased damage from expert, master, or legendary overdrive.

**Source:** `= this.source` (`= this.source-type`)
