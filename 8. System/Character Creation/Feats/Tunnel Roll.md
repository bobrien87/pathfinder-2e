---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Move]]", "[[Surki]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can more easily navigate underground tunnels by rolling up into a ball. You roll up and move up to four times your Speed in a straight line down an incline. If you reach the bottom of the incline or hit an obstacle during this first turn of movement, you stop rolling. Otherwise, you automatically keep rolling at this Speed during subsequent turns until you hit the bottom of the incline or an obstacle ends this movement (which can happen in the middle of your turn). You're [[Slowed]] 2 each turn after the first that you keep rolling; if you hit an obstacle on a turn after the first, you and the obstacle both take 4d6 bludgeoning damage, and you stop rolling.

**Source:** `= this.source` (`= this.source-type`)
