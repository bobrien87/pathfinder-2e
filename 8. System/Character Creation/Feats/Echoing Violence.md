---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Martial Artist|Martial Artist]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]", "[[Death]]", "[[Incapacitation]]"]
prerequisites: "Martial Artist Dedication"
frequency: "once per PT1M"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per minute

**Trigger** You critically succeed with an unarmed Strike against an opponent.

Your powerful attack causes damage that reverberates through your opponent's body, shaking muscle from bone. The creature takes 10d6 bludgeoning damage with a [[Fortitude]] save against your class DC. If it critically fails, it immediately dies as your blow tears apart its body internally.

**Source:** `= this.source` (`= this.source-type`)
