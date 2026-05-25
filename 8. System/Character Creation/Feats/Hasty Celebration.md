---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Emotion]]", "[[Tanuki]]", "[[Visual]]"]
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Trigger** You critically succeed at an attack roll against an enemy, or an enemy critically fails their saving throw against one of your effects.

After even the briefest success, you get caught up in the moment and begin to party, cheering your allies on. You grant all allies within 60 feet a +2 circumstance bonus to attack rolls and damage until the end of your next turn. Unfortunately, while you sing and dance, you aren't keeping an eye on your surroundings like you should, making you [[Off Guard]] to all enemies until the end of your next turn as well.

> [!danger] Effect: Hasty Celebration

**Source:** `= this.source` (`= this.source-type`)
