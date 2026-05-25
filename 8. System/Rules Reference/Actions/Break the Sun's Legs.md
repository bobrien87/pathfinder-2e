---
type: action
source-type: "Remaster"
traits: ["[[Cold]]", "[[Concentrate]]", "[[Darkness]]", "[[Transcendence]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You make a slashing motion over the brightest source of light, whether it's a torch or the sun in the sky. A gash appears over the light source, visible to all, and devours the light. The entire area within a @Template[type:burst|distance:120] around you is affected by a 9th-rank [[Darkness]] spell for 1 minute. The stolen light is channeled to your eyes, granting you greater darkvision for the duration of the effect.

**Source:** `= this.source` (`= this.source-type`)
