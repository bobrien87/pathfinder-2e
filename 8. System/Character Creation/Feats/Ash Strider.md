---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Composite]]", "[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Polymorph]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You discorporate into a cloud of whirling ash and Stride. If you have a fly Speed, you can Fly instead. This movement doesn't trigger reactions, you can move through occupied spaces and tiny cracks, and you ignore any difficult terrain and greater difficult terrain that wouldn't impede smoke. The first creature you pass through during this movement takes @Damage[(floor((@actor.level -6)/2)+3)d6[fire]] damage with a [[Reflex]] save against your class DC. Ash lingers around you after your movement is complete, making you [[Concealed]] until the start of your next turn.

**Level (+2)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
