---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Fortune]]", "[[Mental]]", "[[Reflection]]"]
frequency: "once per PT1M"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per minute

**Trigger** You're about to attempt a saving throw against a mental effect.

You feel a strong connection with your progenitor and can convince yourself an effect targeting your mind was meant for theirs instead, allowing you to shrug off harmful effects. Roll the saving throw twice, and take the higher result. However, subsuming your identity is disturbing, and you're [[Frightened]] 1.

**Source:** `= this.source` (`= this.source-type`)
