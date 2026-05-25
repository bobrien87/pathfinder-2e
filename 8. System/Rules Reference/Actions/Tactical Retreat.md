---
type: action
source-type: "Remaster"
traits: ["[[Emotion]]", "[[Fear]]", "[[Mental]]"]
cast: "`pf2:r`"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You gain the frightened condition

**Frequency** once per hour

**Effect** Realizing that discretion is the better part of valor, you opt to put some distance between you and a threat. You gain the [[Fleeing]] condition until the beginning of your next turn, and you Stride.

**Source:** `= this.source` (`= this.source-type`)
