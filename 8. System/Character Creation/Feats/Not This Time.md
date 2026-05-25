---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Timewracked|Timewracked]]"
source-type: "Remaster"
level: "18"
traits: ["[[Mythic]]", "[[Occult]]"]
prerequisites: "Timewracked Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature targets you with a single-target spell or ability that you defend against with a saving throw or your AC.

You reflexively attempt to cycle a creature's timeline briefly to a reality where it's less able to succeed. Spend a Mythic Point. The creature that targets you must then attempt a [[Will]] save against your class DC or spell DC at mythic proficiency, whichever is higher.
- **Critical Success** The spell or ability affects you normally.
- **Success** The creature's attempt to target you is slightly hindered. If your AC is being targeted, you gain a +2 circumstance bonus to your AC. If you need to attempt a saving throw, you gain a +2 circumstance bonus to the save.
- **Failure** The creature's attempt to target you is significantly hindered. If your AC is being targeted, you gain a +2 circumstance bonus to your AC, and a critical hit against you becomes a normal hit. If you need to attempt a saving throw, you gain a +2 circumstance bonus to the save, and if you critically fail, you fail instead.
- **Critical Failure** The creature's attempt to target you fails, and the actions it used to make the attempt are wasted.

**Source:** `= this.source` (`= this.source-type`)
