---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Minotaur]]", "[[Visual]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The sight of you charging forward into battle emboldens your allies to follow. You Stride up to twice your Speed and make a horns melee Strike. If your Strike hits and damages an enemy, each ally within 60 feet who saw you hit can use a reaction to Stride up to twice their Speed, but each must end their Stride closer to you than where they started. Each such ally that Strides gains a +1 status bonus to their first Strike on their next turn.

**Source:** `= this.source` (`= this.source-type`)
