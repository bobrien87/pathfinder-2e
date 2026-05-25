---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Kineticist]]", "[[Polymorph]]", "[[Primal]]"]
prerequisites: "exactly one kinetic element"
frequency: "once per day"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Requirements** Your kinetic gate is deactivated.

You open your kinetic gate, but rather than activating your kinetic aura, you instead become overwhelmed with transformative elemental energy. You're affected by an [[Elemental Form]] spell with the same trait as your kinetic element. You can heighten it to any spell rank up to half your level rounded up.

**Source:** `= this.source` (`= this.source-type`)
