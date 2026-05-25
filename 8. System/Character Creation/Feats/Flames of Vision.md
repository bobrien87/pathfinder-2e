---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Goblin]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** dokkaebi goblin heritage or Tian Xia origin

Dokkaebi were among the first goblins to pioneer gazing through flames, spectral or physical, to cast their senses far and wide. You can cast [[Clairvoyance]] as a 4th-rank innate occult spell twice per day. To see through the spell's eye, you must be staring into a source of fire.

**Special** If you can cast [[Ignition]], including from the [[Dokkaebi Fire]] feat, then you can cast that spell as part of casting *clairvoyance*. Instead of the cantrip's normal effect, you conjure flames in your hand, which persist for the duration of your *clairvoyance* spell for you to gaze through.

**Source:** `= this.source` (`= this.source-type`)
