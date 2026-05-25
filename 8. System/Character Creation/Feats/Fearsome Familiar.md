---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Primal]]"]
prerequisites: "a familiar"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your familiar trades places with an elemental from its elemental plane. Summon a common creature that has the elemental trait and a level no greater than your level - 4. This creature appears in the same space as your familiar, which disappears for the duration of this impulse. The elemental can appear in a space it can't normally reach. A creature you summon with the Fearsome Familiar feat gains the summoned trait. You can Sustain this impulse up to 1 minute. When the impulse ends, the familiar appears in the space the summoned elemental occupied. A familiar can endure this process only so often-if you use this impulse on your familiar more than once per day, it dies as soon as it returns the second time.

**Source:** `= this.source` (`= this.source-type`)
