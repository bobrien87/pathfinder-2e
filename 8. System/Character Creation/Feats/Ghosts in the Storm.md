---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Air]]", "[[Electricity]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]", "[[Stance]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Clouds, like eager pets, are drawn to you and to those in your good graces. Fast-moving gray clouds surround you, as well as your allies while they're in your kinetic aura. Anyone surrounded by these clouds gains a +2 status bonus to Reflex saves and Acrobatics checks.

When an affected creature uses a move action, clouds dance around it. Until the start of its next turn, it's [[Concealed]], and its Strikes gain the *[[Shock]]* rune.

> [!danger] Effect: Ghosts in the Storm (Move)

**Source:** `= this.source` (`= this.source-type`)
