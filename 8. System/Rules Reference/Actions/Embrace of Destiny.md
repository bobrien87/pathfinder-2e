---
type: action
source-type: "Remaster"
traits: ["[[Mental]]", "[[Spirit]]", "[[Transcendence]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Choose an enemy within 20 feet of you. It must succeed at a [[Will]] save against your class DC or be pulled directly toward you into a square adjacent to you.

**Source:** `= this.source` (`= this.source-type`)
