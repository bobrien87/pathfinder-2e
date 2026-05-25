---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Divine]]", "[[Exemplar]]"]
prerequisites: "Strike Rivers, Seize Winds"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

For the briefest of moments, you can reach into the realm of true gods, gaining the power to shape reality to your will. Once per day, you can create the effects of a divine spell of 8th level or lower. The spell must be common or one to which you otherwise have access, and it costs as many actions as it would typically take to cast. Use your class DC in place of any necessary spell DC and your class DC – 10 in place of any necessary counteract modifier or spell attack modifier.

Because you are creating these effects with your godly might rather than Casting a Spell, they can't be dispelled or counteracted, like [[Strike Rivers, Seize Winds]].

**Source:** `= this.source` (`= this.source-type`)
