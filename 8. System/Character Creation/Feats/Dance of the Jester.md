---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Wayang]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Through your incredible dance skill, you can embody the character of the Jester, able to take control of the shadows of other players on stage (much to your amusement). Attempt a Performance check against the Fortitude DC of a single enemy within 30 feet.
- **Critical Success** Your shadow and the opponent's synchronize, forcing your target to match your movements step for step. You perform any two of the following actions: Drop Prone, Release an object, Stand, Step, or Stride. You must perform two different actions. Your opponent also takes these actions, moving in the same direction as you (for instance, if you Stride north, so does your opponent) or Releasing an object when you do. The target is then temporarily immune to your Dance of the Jester for 1 day.
- **Success** As critical success, except you can take only one action, not two, before your target becomes temporarily immune to your dance, and you cannot move the target into hazardous terrain.

**Source:** `= this.source` (`= this.source-type`)
