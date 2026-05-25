---
type: action
source-type: "Remaster"
traits: ["[[Flourish]]"]
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're wielding a one-handed melee weapon or a melee weapon with the agile or finesse trait

**Effect** Make two Strikes against a target within your reach, one with the required weapon and one with your fist unarmed attack. If both hit the same target, combine their damage for the purposes of its resistances and weaknesses. Apply your multiple attack penalty to each Strike normally.

**Source:** `= this.source` (`= this.source-type`)
