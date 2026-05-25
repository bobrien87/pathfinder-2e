---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Composite]]", "[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]", "[[Stance]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A vortex of sand and dust surrounds you. Each creature inside your kinetic aura (including you) is [[Concealed]] from any creature outside your kinetic aura, and creatures outside the aura are concealed from creatures inside the aura other than you. Your air impulses carry sands that cut at great speed.

When you use a damaging air impulse that affects at least one creature in your kinetic aura, that impulse deals 1 additional slashing damage, or 2 if the impulse has a single target.

**Level (+2)** The extra damage increases by 1, or 2 if the impulse has a single target.

**Source:** `= this.source` (`= this.source-type`)
