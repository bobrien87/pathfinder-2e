---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Exemplar]]"]
frequency: "once per PT1H"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour; see text

Through sheer physical force, you can wrestle a river, lasso the winds, punch a hole to the molten center of the planet, or create other environmental disturbances via nothing but your own strength.

You can create each of the following spell effects at the listed rank, but you can't create effects more than once per hour and you can't perform a given effect more than once per day: **4th** [[Hydraulic Torrent]], **5th** [[Control Water]], **6th** [[Howling Blizzard]], **7th** [[Volcanic Eruption]], **8th** [[Punishing Winds]].

Creating the effects requires the same type and number of actions as Casting the Spell, and they use the higher of your class DC or spell DC when appropriate. Because you are creating these effects with your godly might rather than Casting a Spell, they can't be dispelled or counteracted.

**Source:** `= this.source` (`= this.source-type`)
