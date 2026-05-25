---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Cultivator|Cultivator]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Healing]]", "[[Vitality]]"]
prerequisites: "Cultivator Dedication"
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Trigger** You Cast a focus spell.

Your roots of qi stand firm, shaking off pains and aches like the returning flowers and leaves shed during winter's snow. You @Damage[(@actor.level + @actor.system.resources.focus.max)[healing,vitality]]{regain Hit Points} equal to your level plus the maximum number of Focus Points in your focus pool.

**Source:** `= this.source` (`= this.source-type`)
