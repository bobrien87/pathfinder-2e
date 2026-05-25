---
type: action
source-type: "Remaster"
cast: "`pf2:0`"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** Your turn begins

**Requirements** You are gaining a bonus to damage from Let Death Be My Weapon

**Effect** Spend a Mythic Point. You gain a status bonus to damage equal to double the bonus you're receiving from Let Death Be My Weapon that lasts for 1 minute. During this time, this status bonus doesn't decrease or increase if the value of your doomed, dying, or wounded condition decreases or increases.

**Source:** `= this.source` (`= this.source-type`)
