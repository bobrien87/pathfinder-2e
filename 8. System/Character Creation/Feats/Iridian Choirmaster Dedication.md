---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Iridian Choirmaster|Iridian Choirmaster]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Occultism"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you take this dedication, choose one willing, non-minion ally to be your student in the ways of the Iridian Choir. As part of your training in this archetype, you teach your student the necessary mindset and techniques; they gain the benefits of your abilities without having to take any feats of their own. You gain the benefits of your Iridian Choirmaster archetype feats only if both you and your student are alive and conscious.

You and your student can trade nonverbal messages as a single action, which have the effects of the [[Message]] spell but are non-magical. This requires a single action, has the concentrate, mental, and linguistic traits, and requires that you be able to see each other.

If your student dies, or if you and your student choose to part ways, you can choose and develop a new student by spending 1 week of downtime training another willing, non-minion ally.

**Special** Your student can't be the student of another character with the Iridian Choirmaster Dedication, and if your student takes the Iridian Choirmaster Dedication, they must choose you to be their student.

Iridian Choirmaster

**Source:** `= this.source` (`= this.source-type`)
