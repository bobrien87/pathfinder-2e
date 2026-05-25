---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Leshy]]"]
frequency: "once per P1M"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Once per month, when you die, you can instead choose to fade away. Your corpse is swallowed by the earth, leaving behind only a seed. This seed is very fragile with an AC of 10 and only 1 Hit Point. Another creature can spend 1 minute to plant the seed in a safe space and water it. If so cared for, the next morning a tree grows from it with a single large fruit or flower bud that splits open to reveal you, alive and returned to maximum Hit Points.

**Source:** `= this.source` (`= this.source-type`)
