---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Primal]]", "[[Teleportation]]"]
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per hour

**Effect** You jump through the First World for a brief second, teleporting up 60 feet away to an empty space you can see. If this would bring another creature with you—even if you're carrying it in an extradimensional container—the action is lost.

**Source:** `= this.source` (`= this.source-type`)
