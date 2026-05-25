---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Exploration]]", "[[Extradimensional]]", "[[Occult]]", "[[Wayang]]"]
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can make yourself as flat as a paper doll or shadow. You can spend 1 minute in motionless meditation before performing an odd step that takes you partially out of this plane, leaving your body completely flat. In this state, you can slip under doors, through tiny cracks, or anywhere a single sheet of paper could, but you can't cast spells, activate items, or use actions that have the attack or manipulate traits. You remain in this state for 1 minute unless you choose to return to normal sooner as an action, which has the concentrate trait.

**Source:** `= this.source` (`= this.source-type`)
