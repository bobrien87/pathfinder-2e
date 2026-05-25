---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Polymorph]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Rock overflows from within you to consume your form before cracking open to reveal your body transformed into living stone. You gain 40 temporary Hit Points. You're immune to critical hits and precision damage. You can't be pushed, pulled, or tripped while you're standing on earth or stone. Your earth Elemental Blasts deal an additional 1d10 damage of their normal type. These benefits last until the end of your next turn, but you can Sustain them up to 1 minute. After you gain temporary Hit Points from this impulse, you can't do so again for 10 minutes.

**Level (20th)** You gain 50 temporary Hit Points.

**Source:** `= this.source` (`= this.source-type`)
