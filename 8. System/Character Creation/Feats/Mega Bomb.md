---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Additive]]", "[[Alchemist]]", "[[Manipulate]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can add a highly explosive additive to an alchemical bomb to turn it into a mega bomb. Throwing this bomb takes a 2-action activity instead of a Strike. This isn't a Strike, and you don't make an attack roll. The mega bomb explodes in a @Template[burst|distance:30] within 60 feet. It deals damage as if each creature were the primary target, with a [[Reflex]] save. On a failed save, a creature also takes any extra effects that affect a primary target (such as [[Off Guard]] from bottled lightning). Though all targets in the area take splash damage as primary targets, there is no further splash beyond that area.

**Source:** `= this.source` (`= this.source-type`)
