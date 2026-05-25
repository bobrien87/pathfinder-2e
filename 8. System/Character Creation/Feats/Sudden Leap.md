---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Barbarian]]", "[[Fighter]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Barbarian** You swing at a foe while mid-leap.

**Fighter** You make an impressive leap and swing while you soar.

Make a [[Leap]], [[High Jump]], or [[Long Jump]] and attempt one melee Strike at any point during your jump. Immediately after the Strike, you fall to the ground if you're in the air, even if you haven't reached the maximum distance of your jump. If the distance you fall is no more than the height of your jump, you take no damage and land upright.

When attempting a High Jump or Long Jump during a Sudden Leap, determine the jump distance using Long Jump's rules, and change your maximum distance to double your Speed.

**Special** If you have [[Felling Strike]], you can use Felling Strike instead of a normal Strike. This doesn't change the number of actions Sudden Leap takes.

**Source:** `= this.source` (`= this.source-type`)
