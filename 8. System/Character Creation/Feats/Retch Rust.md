---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You exhale tendrils formed from flakes of rusted metal. All creatures in a @Template[cone|distance:30] take @Damage[(floor((@actor.level -8)/2)+4)d10[slashing]|options:area-damage] damage with a [[Fortitude]] save against your class DC. A metal creature that fails its save also takes @Damage[(floor((@actor.level -8)/2)+2)d4[persistent,slashing]] damage.

**Level (+2)** The cloud's slashing damage increases by 1d10 and the persistent damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
