---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Flourish]]", "[[Monk]]", "[[Occult]]", "[[Water]]"]
prerequisites: "Reflective Ripple Stance"
frequency: "once per PT1M"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per minute

**Requirements** You're in Reflective Ripple Stance.

You dip and spin, unleashing a wide whirlpool of water. Make an Athletics check to [[Trip]] each creature standing on the ground in a @Template[type:emanation|distance:10]. These attacks all count toward your multiple attack penalty, but the penalty doesn't increase until after you make all the attacks.

**Source:** `= this.source` (`= this.source-type`)
