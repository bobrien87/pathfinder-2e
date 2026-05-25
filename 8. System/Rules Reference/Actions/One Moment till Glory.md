---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Mental]]", "[[Transcendence]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You rally your allies, carrying them from the brink of disaster to the verge of victory. Each ally in your aura can immediately attempt a new saving throw with a +2 status bonus against one ongoing negative effect or condition currently affecting it that required a save. Use the result of the new save to determine the outcome of the effect, unless the new save would have a worse result than the original save, in which case nothing happens. Each ally can gain this benefit against a given effect only once.

> [!danger] Effect: One Moment till Glory

**Source:** `= this.source` (`= this.source-type`)
