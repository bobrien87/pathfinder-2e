---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Centaur]]"]
prerequisites: "budding speaker centaur heritage or Speaker in Training"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're among the most powerful of Speakers and can adopt the form of the spirits you entreat with. Select one of the following spells, which you can cast once per day as a 7th-rank innate spell. If you're a Faithspeaker, select from [[Angel Form]], [[Daemon Form]], [[Demon Form]], or [[Devil Form]], which you cast as a divine spell; if you're a Greenspeaker, select from [[Elemental Form]] or [[Plant Form]], which you cast as a primal spell.

**Source:** `= this.source` (`= this.source-type`)
