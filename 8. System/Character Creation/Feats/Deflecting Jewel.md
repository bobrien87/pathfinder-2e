---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Occult]]", "[[Sarangay]]"]
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Trigger** You're the target of a ranged attack while you possess your head gem.

**Requirements** You're aware of the triggering attack.

You walk the line between two sides of something, such as belonging to two clans, having a mixed allegiance or faith, or being caught between two possible fates. Your dual nature has attuned your head gem to the half moon, and it has manifested the power to ward away attacks by drawing a line between them and you. You gain a +2 circumstance bonus to AC against the triggering attack.

**Source:** `= this.source` (`= this.source-type`)
