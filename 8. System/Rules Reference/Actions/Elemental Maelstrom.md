---
type: action
source-type: "Remaster"
traits: ["[[Eidolon]]"]
cast: "`pf2:3`"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Your eidolon temporarily shifts its form into a swirling vortex of elemental matter and rampages through their foes. Your eidolon Strides. During their movement, they can attempt a Strike against each enemy that is within their reach. If an enemy comes within your eidolon's reach more than once, your eidolon makes only a single Strike against a given enemy. These attacks all count towards your eidolon's multiple attack penalty, but the penalty doesn't increase until after all the attacks. If your eidolon has the appropriate Speed, they can Climb, Fly, or Swim instead of Stride.

**Source:** `= this.source` (`= this.source-type`)
