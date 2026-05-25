---
type: action
source-type: "Remaster"
traits: ["[[Transcendence]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You move with a speed belying your strength, carrying your allies as easily as straw dolls. You Stride. At any point you are adjacent to a willing ally during the Stride, you can pick that ally up, and you can deposit them into a space adjacent to you at any other point during your movement. You ignore the ally's Bulk while carrying them during your Stride. You can Climb, Fly, or Swim instead of Striding if you have the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
