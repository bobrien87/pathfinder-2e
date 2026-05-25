---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Divine]]", "[[Linguistic]]", "[[Mental]]"]
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You share a story of your travels with a creature within 30 feet. You gain the blessing of Isthralei as a +1 status bonus to AC and Will saves until the end of your next turn. On their next turn, the creature you shared a story with can take a single action, which has the auditory, concentrate, linguistic, and mental traits, to respond with their own story to gain the same benefits until the end of the following turn.

> [!danger] Effect: Offer Story

**Source:** `= this.source` (`= this.source-type`)
