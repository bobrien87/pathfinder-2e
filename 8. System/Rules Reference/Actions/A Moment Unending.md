---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Prediction]]", "[[Transcendence]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You take in every movement around you, affording you unparalleled accuracy. Your next successful Strike against an enemy before the end of your next turn deals an additional 1d6 precision damage. This damage increases to 2d6 at 10th level and 3d6 at 18th level.

**Source:** `= this.source` (`= this.source-type`)
