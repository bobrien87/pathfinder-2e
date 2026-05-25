---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Monk]]", "[[Stance]]"]
prerequisites: "Monastic Weaponry"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You enter a mindful stance that creates a deep connection between you and your monk weapons, allowing you to manipulate them with your qi, even at a distance. All melee monk weapons you wield with the finesse trait gain the thrown 10 feet trait (unless they already have the thrown trait with a greater range).

Once you've made a thrown Strike with such a weapon, you can use the precision of your throw to make additional strikes with it, even from a distance. Start from the space of the previous Strike's target to determine the range increment and whether the new target has cover. At the end of your turn, the thrown weapon flies directly back to you in a straight line. If a solid barrier blocks its path, it falls to the ground after hitting the barrier.

**Source:** `= this.source` (`= this.source-type`)
