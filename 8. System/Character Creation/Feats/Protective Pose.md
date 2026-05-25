---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Manipulate]]", "[[Summoner]]"]
prerequisites: "trained in Medicine"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Tian Xia origin

**Requirements** You and your eidolon are within 30 feet of one another.

Many physical poses can fortify one's health, but some poses need more than one body to accomplish. As you and your eidolon pose in tandem, you each channel qi into a protective barrier in a @Template[type:emanation|distance:30] until the start of your next turn. Creatures within range of either you or you eidolon gain resistance to your choice of acid, cold, electricity, fire, or sonic damage equal to half your level. In addition, any Medicine check targeting a creature with this resistance gets a +1 status bonus (or a +2 status bonus if you're a master in Medicine).

> [!danger] Effect: Protective Pose

**Source:** `= this.source` (`= this.source-type`)
