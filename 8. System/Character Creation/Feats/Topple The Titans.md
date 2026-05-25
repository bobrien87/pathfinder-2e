---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Exemplar]]"]
frequency: "once per PT1M"
source: "Pathfinder #217: Death Sails a Wine-Dark Sea"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** Once per minute

**Requirements** Your previous action was a successful or critically successful [[Trip]] against a creature at least one size larger than you, and the enemy became [[Prone]].

Even the greatest titans of the world are easier to kill when they're lying on the ground. You've made it your mission to topple such giants and can make others fall with a force that shakes the very earth. The triggering creature's toppling body shakes the ground, emitting a quake in a @Template[type:emanation|distance:10] from their space. Apply the result of your triggering Athletics check against the Reflex DC of each creature in the emanation to Trip them as well. You do not need to have a hand free, and you do not lose your balance if any of your attempts to Trip are a critical failure.

**Source:** `= this.source` (`= this.source-type`)
