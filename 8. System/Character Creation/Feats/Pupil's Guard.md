---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Iridian Choirmaster|Iridian Choirmaster]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Concentrate]]"]
prerequisites: "Iridian Choirmaster Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** Your student would be targeted with a reaction (such as Reactive Strike) due to their Stride or manipulate action.

**Requirements** You're adjacent to your student.

You're intimately familiar with your student's motions and are ready to step in at a moment's notice should anything threaten to disrupt them. You interpose yourself between the attack and your student, becoming the target of the reaction and taking all damage and associated effects (if any) yourself. This allows your student to complete their action without interruption.

**Source:** `= this.source` (`= this.source-type`)
