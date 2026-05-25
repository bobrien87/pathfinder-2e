---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Alchemist]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can lob bombs with great force and a precise trajectory to angle the splash in a cone that sprays in a single direction, potentially allowing you to avoid allies and splash deeper into enemy lines. When throwing an alchemical bomb with the splash trait, instead of splashing all squares adjacent to the target, you can create a splash in a @Template[cone|distance:15]. You choose the cone's direction, but its first square must be a square in the target's space.

**Special** If you have the [[Expanded Splash]] feat or another ability that increases the radius of splash damage, you can have the splash damage be a @Template[cone|distance:20].

**Source:** `= this.source` (`= this.source-type`)
