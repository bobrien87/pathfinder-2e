---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Swashbuckler]]"]
prerequisites: "expert in Athletics"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your panache allows you to perform incredible feats: climbing, swimming, and leaping far beyond your normal capacity. While you have [[Panache]], you gain the following benefits.

- You gain climb and swim Speeds equal to half your land Speed.
- The DCs of your [[High Jumps]] and [[Long Jumps]] decrease by 10. This doesn't combine with other abilities that reduce those DCs.
- The distance you can move with a vertical [[Leap]] increases to 5 feet. Your distance for a horizontal Leap increases to 15 feet if your Speed is at least 15 feet, or to 20 feet if your Speed is at least 30 feet.

**Source:** `= this.source` (`= this.source-type`)
