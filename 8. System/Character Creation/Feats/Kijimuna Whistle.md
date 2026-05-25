---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Gnome]]"]
prerequisites: "kijimuna gnome heritage or at least one primal innate spell from a gnome heritage or feat"
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** kijimuna gnome heritage or Tian Xia origin

Your connection to nature—and trees, in particular—has become so strong that you can summon the plants you befriended in the forests of your youth. Once per day, you can whistle the distinct, cheery sound that's a signature of the kijimuna gnome community to cast [[Summon Plant or Fungus]] as a 5th-rank primal innate spell. The spell loses the manipulate trait as the incantations and gestures used for this spell involve only whistling. Nearby kijimuna gnomes automatically recognize this celebratory trill and will usually answer or join in the music making if they can.

**Source:** `= this.source` (`= this.source-type`)
