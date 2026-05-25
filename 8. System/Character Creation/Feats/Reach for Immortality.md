---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Exemplar]]"]
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Your divine spark is now a bonfire in your soul, bringing you to the very cusp of undying immortality. You cease aging. When you would die for any reason, you can Spark Transcendence as a free action that can be taken at any time, regardless of your current condition. You reach for your divine spark and seize it in your hand to survive at 0 Hit Points, purging yourself of any negative conditions. Invigorated by this return to life, you then heal yourself for half of your total Hit Points, Stand, instantly summon any held ikons to your hand, and Shift your Immanence to any of your ikons.

**Source:** `= this.source` (`= this.source-type`)
