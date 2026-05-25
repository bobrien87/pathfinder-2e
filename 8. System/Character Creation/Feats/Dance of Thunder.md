---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Concentrate]]", "[[Gunslinger]]"]
frequency: "once per PT1M"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per minute

**Requirements** You're wielding a loaded firearm or crossbow and are not [[Fatigued]].

Your steps echo with the thunderous retort of exploding black powder as you dance a dance of death. Take any of the following actions you choose in any order: Step, Strike against a target within your firearm's first range increment, and Interact to reload. If you attempted a Strike and it succeeded, you can repeat these three actions again in any order. If you attempted a Strike in the second set and succeeded, you can repeat the actions one last time.

After using Dance of Thunder, you become fatigued for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
