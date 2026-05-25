---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Manipulate]]", "[[Polymorph]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Opening your kinetic gate, you allow flames to consume your form and leave you a living flame. You gain the benefits of the [[Fiery Body]] spell (except the ability to cast ignition) until the end of your next turn. You can Sustain the impulse up to 1 minute, and when you do, you can Fly up to half your fly Speed. Your fire Elemental Blasts deal an additional die of damage.

**Level (16th)** This duration is 1 minute, you can't Sustain the impulse, and you can Dismiss the impulse.

**Source:** `= this.source` (`= this.source-type`)
