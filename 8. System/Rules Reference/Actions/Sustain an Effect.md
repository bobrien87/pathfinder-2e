---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Exploration]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You Sustain one effect with a sustained duration while moving at half speed. Most such effects can be sustained for 10 minutes, though some specify they can be sustained for a different duration. Sustaining an effect that requires making complex decisions, such as [[Spiritual Armament]], can make you [[Fatigued]], as determined by the GM.

**Source:** `= this.source` (`= this.source-type`)
