---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Teleportation]]"]
cast: "Passive"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

10 minutes. You and up to 6 willing creatures you're touching are instantly transported into your *runewell*, regardless of any distance between you and your anima focus.

**Source:** `= this.source` (`= this.source-type`)
