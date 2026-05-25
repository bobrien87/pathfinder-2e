---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Warshard Warrior|Warshard Warrior]]"
source-type: "Remaster"
level: "16"
traits: ["[[Attack]]", "[[Mythic]]"]
prerequisites: "Warshard Warrior Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a ranged warshard weapon.

You can fire a single shot that penetrates multiple foes. Spend 1 Mythic Point, then fire a single shot from your ranged warshard weapon. You inflict your weapon's damage on all creatures in a line, to a maximum distance equal to your weapon's maximum range or until the line hits a solid object that's either thicker than 5 feet or has a Hardness in excess of 20, whichever comes first. Each creature in the area attempts a [[Reflex]] save against your class DC or spell DC, whichever is higher, calculated at mythic proficiency. For each range increment beyond the first, a creature gains a cumulative +2 circumstance bonus to their Reflex save. This ability counts as two attacks when calculating your multiple attack penalty.

**Source:** `= this.source` (`= this.source-type`)
