---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]", "[[Stance]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

As a candle can light another, you awaken the latent potential to channel fire in other creatures. You shed faint, glowing embers, as do your allies while they're in your kinetic aura. Anyone shedding these embers gains a +1 status bonus to Reflex saves and Acrobatics checks and can Step as a free action once per round. When an affected creature takes a move action, its Strikes deal an extra 2 fire damage until the end of its turn.

> [!danger] Effect: Stance: Kindle Inner Flames

**Level (12th)** The status bonus to Reflex saves and Acrobatics checks is +2, and the Strikes gain the *[[Flaming]]* rune instead of the extra 2 fire damage.

**Source:** `= this.source` (`= this.source-type`)
