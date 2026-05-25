---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Exploration]]", "[[Linguistic]]", "[[Mental]]"]
cast: "Passive"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You spend 10 minutes conferring with one of your knights who has the doomed condition. By discussing plans for your future kingdom with them and describing the benefits of your rule, you can attempt to soothe their spirits. Attempt a Diplomacy or Society check against a hard DC of your knight's level. Regardless of the result, that knight gains the benefits of the Refocus activity (if they have a focus pool) but is temporarily immune to Royal Grace for 24 hours.
- **Critical Success** The knight's doomed condition is reduced by 2 (minimum 0).
- **Success** The knight's doomed condition is reduced by 1 (minimum 0).
- **Failure** The knight's doomed condition isn't reduced.

**Source:** `= this.source` (`= this.source-type`)
