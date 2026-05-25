---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

An artificial metal object forms in the hands of you or a willing ally within 30 feet. You can choose a level 0, common, handheld weapon or piece of adventuring gear of 1 Bulk or less. The item is entirely made from metal, making some items impossible or impractical to use (if it's unclear, the GM decides). You can make items with simple moving parts or magnetism, like a compass, poor lock, or merchant's scale. The item lasts for 10 minutes, but each time it's used, the user must succeed at a DC 5 flat check or the item is destroyed after the action is completed.

**Source:** `= this.source` (`= this.source-type`)
