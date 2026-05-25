---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Monk]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You defy gravity, traversing vertical planes as easily as the ground. Stride up to your Speed. You must start your movement on a horizontal surface.

During this movement, you can run up vertical surfaces, like walls, at your full Speed. If you end the Stride off the ground, you fall after taking your next action or when your turn ends, whichever comes first (though you can [[Grab an Edge]], if applicable).

If you have [[Water Step]] or a similar ability, Wall Run lets you run along flimsy vertical surfaces, as well as vertical liquids, such as a waterfall.

**Source:** `= this.source` (`= this.source-type`)
