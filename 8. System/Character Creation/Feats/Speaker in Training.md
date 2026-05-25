---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Centaur]]"]
prerequisites: "budding speaker centaur heritage or the ability to cast a divine or primal spell"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've begun your training as a Speaker. Select divine or primal. If you selected divine, you're a Faithspeaker. If you selected primal, you're a Greenspeaker. If you've already made this decision (such as due to being a budding speaker) you must select the same Speaker you previously chose. This choice can't be changed. If you're a Faithspeaker, you can cast [[Bless]] once per day as a divine innate spell; if you're a Greenspeaker, you can cast [[Fleet Step]] once per day as a primal innate spell.

**Source:** `= this.source` (`= this.source-type`)
