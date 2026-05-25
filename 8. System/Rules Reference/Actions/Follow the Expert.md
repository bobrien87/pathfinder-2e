---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Exploration]]", "[[Visual]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Choose an ally attempting a recurring skill check while exploring, such as climbing, or performing a different exploration tactic that requires a skill check (like [[Avoiding Notice]]). The ally must be at least an expert in that skill and must be willing to provide assistance. While Following the Expert, you match their tactic or attempt similar skill checks.

Thanks to your ally's assistance, you can add your level as a proficiency bonus to the associated skill check, even if you're untrained. Additionally, you gain a circumstance bonus to your skill check based on your ally's proficiency (+2 for expert, +3 for master, and +4 for legendary).

> [!danger] Effect: Follow The Expert

**Source:** `= this.source` (`= this.source-type`)
