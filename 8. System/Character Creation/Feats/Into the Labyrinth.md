---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Minotaur]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Calling on your connection to minotaurs of myth, you shunt an enemy into a complex maze full of puzzles of your own devising. Once per day, you can cast [[Quandary]] as an 8th-rank occult innate spell, which takes the form of a labyrinth instead of a puzzle room. Targets cannot attempt to use Occultism to escape the spell (as normal for *quandary*), but they can use Survival to find their way through the labyrinth's corridors.

**Source:** `= this.source` (`= this.source-type`)
