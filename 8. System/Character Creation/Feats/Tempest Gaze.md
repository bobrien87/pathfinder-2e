---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Hungerseed]]"]
prerequisites: "Storming Gaze"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your third eye grows stronger and more powerful. When you use Storming Gaze, you can increase the area to a @Template[type:cone|distance:30] and @Damage[(ceil(@actor.level/2))d4[electricity],(ceil(@actor.level/2))d4[sonic]|options:area-damage]{double the number of damage dice}; half deal electricity damage, and half deal sonic damage. If you Storming Gaze in this way, you can't use it again for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
