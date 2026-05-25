---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Swashbuckler]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You take damage that would reduce you to 0 Hit Points.

Somehow you always escape the reaper by a hair's breadth. You avoid being knocked out or killed and remain at 1 Hit Point and gain panache, but you become [[Doomed]] 1 (or increase your doomed value by 1 if you were already doomed).

You can't reduce or ignore the doomed condition from Cheating Death. The doomed condition from Cheating Death lasts for 10 minutes, though this doesn't affect the duration of any other doomed condition you have.

**Source:** `= this.source` (`= this.source-type`)
