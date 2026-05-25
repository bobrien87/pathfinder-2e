---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Monk]]"]
prerequisites: "Rushing Goat Stance"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're in [[Rushing Goat Stance]].

You attack in an unceasing flurry of charging headbutts. Stride or Climb and then make a ramming horn Strike. If the Strike is successful, you immediately push the target back 10 feet, then Stride or Climb and make a second ramming horn Strike against them. If the second Strike is successful, you immediately knock the target [[Prone]], but if the second Strike is a failure or if you're unable to complete all the required actions, you become [[Stunned]] 1.

Both Strikes count toward your multiple attack penalty, but the penalty doesn't increase until you've made both of them.

**Source:** `= this.source` (`= this.source-type`)
