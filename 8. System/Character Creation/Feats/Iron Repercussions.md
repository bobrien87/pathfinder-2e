---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Champion]]"]
prerequisites: "obedience cause"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Disobeying your [[Iron Command]] has lasting consequences. If an enemy refuses to kneel to you, you can deal @Damage[(ternary(gte(@actor.level,19),6,ternary(gte(@actor.level,16),5,ternary(gte(@actor.level,12),4,ternary(gte(@actor.level,9),3,ternary(gte(@actor.level,5),2,1))))))d6[persistent,mental]]{persistent mental damage} instead of normal mental damage. You must decide whether the mental damage will be persistent before your enemy chooses whether to kneel or not. The amount of damage is unchanged.

**Source:** `= this.source` (`= this.source-type`)
