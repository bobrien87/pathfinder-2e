---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Minotaur]]"]
prerequisites: "expert in Athletics, Friendly Nudge"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With your large size, you need to be careful around your smaller friends. You have learned to move in such a way that it gives others the chance to make room for you. Stride up to your Speed. If you end your movement in a position where one or more of your spaces are occupied by an ally, each of those allies can immediately Step as a free action so that they are no longer occupying the same space as you. If this isn't possible, you must end your movement so that you aren't sharing a space with an ally, as normal.

**Source:** `= this.source` (`= this.source-type`)
