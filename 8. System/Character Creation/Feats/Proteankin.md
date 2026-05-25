---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Lineage]]", "[[Nephilim]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your blood bubbles with the roiling quintessence of the Maelstrom, the infinite sea of primal chaos that long ago spawned the other Outer Planes. You gain resistance to a single damage type equal to half your level; at the beginning of each day, determine randomly whether this resistance applies to acid, electricity, or sonic damage. You also gain a +1 circumstance bonus to saving throws against effects that would cause you to gain the controlled condition.

**Source:** `= this.source` (`= this.source-type`)
