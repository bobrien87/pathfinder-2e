---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Aldori Duelist|Aldori Duelist]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Stance]]"]
prerequisites: "Aldori Duelist Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding only an [[Aldori Dueling Sword]] and have your other hand or hands free; you are not [[Fatigued]].

Many assume that a duelist's habit of fighting with one hand behind their back or on their hip is an insult or self-restriction. This could not be further from the truth. Fighting with a single hand dictates mastery and heightens the duelist's focus by narrowing points of interest, allowing them to move and react to changing situations with unnatural speed. While in this stance, you are [[Quickened]]. You can use this extra action only to Step or use a single-action activity gained from the Aldori duelist archetype. If you use your free hand for anything, this stance ends. When this stance ends, you become fatigued until you rest for at least 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
