---
type: action
source-type: "Remaster"
traits: ["[[Transcendence]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** Your previous action was to Strike with the [[Unfailing Bow]]

**Effect** You repeat your motions exactly, your attack landing in the same location as your previous shot. You make a Strike against the same target. The result of your d20 roll is the same as the result of the required shot, though any penalties (such as your multiple attack penalty) apply normally to this shot and you don't automatically adjust the degree of success if the initial roll was a natural 1 or 20.

**Source:** `= this.source` (`= this.source-type`)
