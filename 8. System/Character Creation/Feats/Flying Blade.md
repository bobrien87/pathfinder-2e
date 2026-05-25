---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Swashbuckler]]"]
prerequisites: "precise strike"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You apply your flashy techniques to thrown weapons as easily as melee attacks. You apply your [[Precise Strike]] damage on ranged Strikes you make with a thrown weapon within that weapon's first range increment. The thrown weapon must be an agile or finesse weapon. This also allows you to make a thrown weapon ranged Strike for [[Confident Finisher]] and any other finisher that includes a Strike that can benefit from your precise strike.

**Source:** `= this.source` (`= this.source-type`)
