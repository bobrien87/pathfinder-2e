---
type: action
source-type: "Remaster"
traits: ["[[Spirit]]", "[[Transcendence]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Your spirit is so dense it takes on tangible force. Make a melee Strike with the [[Titan's Breaker]]. This counts as two attacks when calculating your multiple attack penalty. If this Strike hits, your additional spirit damage from the ikon's immanence increases to 4 plus an extra die of weapon damage.

If you're at least 10th level, it's increased to 6 spirit damage and two extra dice, and if you're at least 18th level, it's increased to 8 spirit damage and three extra dice.

**Source:** `= this.source` (`= this.source-type`)
