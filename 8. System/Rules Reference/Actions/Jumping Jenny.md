---
type: action
source-type: "Remaster"
cast: "`pf2:1`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Target a flying creature within 60 feet. Until the start of your next turn, each time that creature attempts to Fly, they must succeed at an Acrobatics check to `act maneuver-in-flight` against the DC of [[Launch Fireworks]], or the Fly action is disrupted. If all the creature's attempts to Fly are disrupted, at the end of its turn, it falls harmlessly to the ground below.

**Source:** `= this.source` (`= this.source-type`)
