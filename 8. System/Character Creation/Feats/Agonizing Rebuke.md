---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Hobgoblin]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you terrorize your enemies, you also cause them painful mental distress. When you successfully [[Demoralize]] an enemy, that enemy takes @Damage[ternary(gte(@actor.system.skills.intimidation.rank,4),3,ternary(gte(@actor.system.skills.intimidation.rank,3),2,1))d4[mental]] damage at the start of each of its turns. This effect ends if the creature loses the frightened condition, if it is more than 30 feet away from you, or if 1 minute passes, whichever comes first. If you have master proficiency in Intimidation, the damage increases to 2d4, and if you have legendary proficiency, the damage increases to 3d4.

**Source:** `= this.source` (`= this.source-type`)
