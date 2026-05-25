---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Athamaru]]"]
prerequisites: "Emit Defensive Odor"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've mastered your defensive pheromones and have nearly complete control over them. When you Emit Defensive Odor, you can either choose to increase the damage dealt to a single target by changing the damage dice to d8s (@Damage[(floor((@actor.level +1)/2)+1)d8[poison]|options:area-damage]), or leave the damage unchanged but spray your pheromones in a @Template[cone|distance:15].

**Source:** `= this.source` (`= this.source-type`)
