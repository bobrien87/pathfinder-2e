---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Healing]]", "[[Kitsune]]", "[[Vitality]]"]
prerequisites: "Star Orb"
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You or an ally within 30 feet of your [[Star Orb]] familiar would be reduced to 0 Hit Points but not immediately killed.

You temporarily drain your star orb familiar's energy to save an ally. The target avoids being knocked out and remains at 1 Hit Point, and their [[Wounded]] condition increases by 1. The target then @Damage[@actor.level[healing,vitality]]{regains Hit Points} equal to your level. When the familiar's energy is drained, it becomes dormant until your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
