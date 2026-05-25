---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Barbarian]]"]
prerequisites: "expert in Athletics"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Physical obstacles can't hold back your fury. While you are raging, you gain a climb Speed and swim Speed equal to your land Speed, the DC of your [[High Jumps]] and [[Long Jumps]] decreases by 10, and you increase your distance on a successful Long Jump by 10 feet. Your distance for a vertical [[Leap]] increases to 5 feet vertically, and your distance for a horizontal Leap increases to 15 feet if your Speed is at least 15 feet, and to 20 feet if your Speed is at least 30 feet.

**Source:** `= this.source` (`= this.source-type`)
