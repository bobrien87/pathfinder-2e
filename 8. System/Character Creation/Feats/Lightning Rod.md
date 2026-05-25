---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Composite]]", "[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You smash a metal rod into your foe and call lightning to it. Attempt a 2-action melee or ranged Elemental Blast using the metal element. On a hit, the target takes an additional @Damage[(floor((@actor.level -6)/6)+1)d12[electricity]] damage and is skewered with a metal rod, which gives it a –1 circumstance penalty to AC and saves against electricity; the penalty is –2 if the creature also has the metal trait, is made of metal, or is wearing metal armor. The creature can attempt to pull the rod free using an Interact action, but must succeed at a DC 10 [[Athletics]] check.

**Level (+6)** The electricity damage increases by 1d12.

**Source:** `= this.source` (`= this.source-type`)
