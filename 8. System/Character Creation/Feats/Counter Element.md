---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Impulse]]", "[[Kineticist]]"]
prerequisites: "exactly one kinetic element"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You're targeted by or in the area of an effect that has the trait matching your kinetic element and originates from an enemy or hazard.

Your absolute dedication to a single element lets you attempt to gain control over it, even when the element is in service to another entity. You attempt to counteract the effect, using your kineticist class DC - 10 as your counteract check modifier and half this impulse's level rounded up as the counteract rank. If you counteract the effect, you protect only yourself unless you got a critical success on your counteract check.

**Level (12th)** If you successfully counteract the effect, you can have it target or affect a different creature within 30 feet of you. If you got a critical success on the counteract check, you can choose the effect's targets or entire area.

**Source:** `= this.source` (`= this.source-type`)
