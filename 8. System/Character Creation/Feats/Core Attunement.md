---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Automaton]]"]
prerequisites: "mage automaton"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your core allows you to draw more power from it. Select one 1st-rank arcane spell and one 2nd-rank or lower arcane spell, to which you have access. You can cast your chosen spells as arcane innate spells each once per day.

**Enhancement** Your attunement grows stronger. Select one 5th-rank or lower arcane spell and one 6th-rank or lower arcane spell, to which you have access. You can cast them as arcane innate spells each once per day, in addition to the original spells.

**Source:** `= this.source` (`= this.source-type`)
