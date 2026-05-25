---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Air]]", "[[Auditory]]", "[[Illusion]]", "[[Impulse]]", "[[Kineticist]]", "[[Linguistic]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You speak in a whisper, a soft wind carrying your words far away. This has the effect of the [[Message]] spell with a range of 500 feet, and it can target only a creature surrounded by air. If you start your message with the target's name, you and the target don't need to be able to see each other, nor do you need line of effect.

**Level (4th)** The range is 1 mile.

**Level (14th)** The range is planetary plus the Plane of Air.

**Source:** `= this.source` (`= this.source-type`)
