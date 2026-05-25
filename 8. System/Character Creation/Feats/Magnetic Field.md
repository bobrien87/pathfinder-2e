---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Primal]]", "[[Stance]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A magnetic field surrounds you. Choose a polarity when you take this action. You can switch the polarity as a free action at the start of each of your turns while you remain in this stance.

**Attract** A creature that is wearing metal armor, has the metal trait, or is made of metal treats squares in your kinetic aura as difficult terrain when moving away from you. You pull unattended metal objects of light Bulk or less in your kinetic aura to you. They gather in your space and move with you.

**Repel** A creature that is wearing metal armor, has the metal trait, or is made of metal treats squares in your kinetic aura as difficult terrain when moving closer to you. You push unattended metal objects of light Bulk or less in your kinetic aura away. They stop moving once they're outside your aura.

**Source:** `= this.source` (`= this.source-type`)
