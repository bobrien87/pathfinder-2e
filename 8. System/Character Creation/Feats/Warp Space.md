---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Amp]]", "[[Psychic]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You use your magic to bend space, causing your spell to strike from a strange vector. Use this amp in place of a psi cantrip's normal amp entry. The amped psi cantrip must have a range.

**Amp** Choose a square within 30 feet to which you have line of effect and line of sight. Determine your spell's line of effect and line of sight from there, as well as whether creatures have cover against the spell. The spell can exceed its normal range as measured from you, as long as it's within its normal range from the square you chose.

**Source:** `= this.source` (`= this.source-type`)
