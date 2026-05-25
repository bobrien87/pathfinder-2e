---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Oracle]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are [[Cursebound 4]].

Your mind and body can, for a short time and with great peril, surpass the final limits of your curse. For 1 minute, you shed torrential flames, become surrounded by spirits, or otherwise overflow with divine power in a way that suits your mystery. On each of your turns during that time, you can cast one revelation spell without spending Focus Points.

At the end of the minute, the durations of any revelation spells you cast during that time end, and you must attempt a DC 40 [[Fortitude]] save.
- **Critical Success** You aren't otherwise affected.
- **Success** You are [[Drained]] 2 and can't reduce or remove this condition until your next preparations.
- **Failure** You are [[Drained]] 4 and can't reduce or remove this condition until your next preparations.
- **Critical Failure** You die.

**Source:** `= this.source` (`= this.source-type`)
