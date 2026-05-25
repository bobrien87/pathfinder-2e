---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Air]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A blade of shearing wind races away from you in a @Template[line|distance:60]. Each creature in the area takes @Damage[(floor((@actor.level -1)/2) +2)d4[slashing]|options:area-damage] damage with a [[Reflex]] save against your class DC. In the final square of the line, the boomerang whirls in place until the end of your next turn. Any creature that ends its turn in that square has to save against the boomerang.

On your next turn, you can use a single action, which has the concentrate trait, to return the boomerang to you. It returns in a line from its square to your current location, with the same effect as the initial line, then the impulse ends. You must have line of effect to the boomerang and be within 60 feet of it.

**Level (+2)** The damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
