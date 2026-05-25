---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Athamaru]]", "[[Inhaled]]", "[[Poison]]"]
frequency: "once per day"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

While athamarus' natural pheromones are typically used for communication, you have developed yours into a defense mechanism to ward off foes. You emit a thick spray of defensive pheromones at an adjacent creature, who takes @Damage[(floor((@actor.level +1)/2)+1)d6[poison]] damage with a [[Fortitude]] save against your class DC.

At 3rd level and every 2 levels thereafter, the damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
