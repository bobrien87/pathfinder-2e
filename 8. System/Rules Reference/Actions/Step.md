---
type: action
source-type: "Remaster"
traits: ["[[Move]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** Your Speed is at least 10 feet.

You carefully move 5 feet. Unlike most types of movement, Stepping doesn't trigger reactions, such as [[Reactive Strike]], that can be triggered by move actions or upon leaving or entering a square.

You can't Step into difficult terrain, and you can't Step using a Speed other than your land Speed.

**Source:** `= this.source` (`= this.source-type`)
