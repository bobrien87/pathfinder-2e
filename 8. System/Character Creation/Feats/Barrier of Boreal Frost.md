---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Cold]]", "[[Impulse]]", "[[Kineticist]]", "[[Manipulate]]", "[[Overflow]]", "[[Primal]]", "[[Water]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You form an intricate structure of ice, such as a wall of bricks made of packed snow or a screen of enormous icicles. This has the effect of a [[Wall of Ice]] spell with a spell rank equal to half your level rounded up. It can only be a wall (not a hemisphere), and you choose whether the ice is transparent or opaque. The wall lasts until the end of your next turn, but you can Sustain it up to 1 minute.

**Source:** `= this.source` (`= this.source-type`)
