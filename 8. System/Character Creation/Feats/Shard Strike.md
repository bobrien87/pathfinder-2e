---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Jagged metal shards form in the air and lash out from you. You choose shards or spines, which changes the area, damage type, and critical failure effect. Each creature in the area attempts a [[Reflex]] save against your class DC.

**Shards** Shards deal @Damage[(floor((@actor.level -1)/2)+1)d6[slashing]|options:area-damage] damage in a @Template[cone|distance:15], and a creature that critically fails takes 1d6 bleed damage.

**Spines** Spines deal @Damage[(floor((@actor.level -1)/2)+1)d6[piercing]|options:area-damage] damage in a @Template[line|distance:30], and a creature that critically fails is [[Clumsy]] 1 until the start of your next turn.

**Level (+2)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
