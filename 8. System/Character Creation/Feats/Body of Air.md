---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Air]]", "[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Polymorph]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

R or `pf2:2`

**Trigger** An enemy you can observe targets you with an attack or other damaging effect.

Your gathered air consumes your body, leaving only a cloud of living vapor. This has the same effects on you as [[Vapor Form]]. The effect lasts until the end of your next turn, but you can Sustain the form up to 5 minutes. If you activate your kinetic aura, Body of Air ends.

You can use Body of Air as a reaction only when the trigger is met, but you can use it as a 2-action activity without the trigger being met.

**Level (+1)** The resistance increases by 1.

**Source:** `= this.source` (`= this.source-type`)
