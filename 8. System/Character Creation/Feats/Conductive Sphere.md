---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Electricity]]", "[[Impulse]]", "[[Kineticist]]", "[[Manipulate]]", "[[Metal]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A floating metal ball forms in a space within 30 feet, flashing with electricity. It can't be targeted or damaged. Any of your allies adjacent to it gain resistance to electricity equal to your level and add the *[[Shock]]* rune to all their Strikes with metal objects. The sphere lasts until the end of your next turn, but you can Sustain it up to 1 minute.

When you conjure the sphere and the first time you Sustain the impulse on subsequent rounds, you can either have it Fly up to 20 feet or deal @Damage[(floor((@actor.level - 5)/3))d12[electricity]] damage to an adjacent creature with a [[Reflex]] save against your class DC.

> [!danger] Effect: Conductive Sphere

**Level (+3)** The damage dealt by the sphere increases by 1d12.

**Source:** `= this.source` (`= this.source-type`)
