---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Crossbow Infiltrator|Crossbow Infiltrator]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Flourish]]", "[[Manipulate]]"]
prerequisites: "Crossbow Infiltrator Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding an unloaded hand crossbow or an unloaded gauntlet bow.

You can fire off a single shot even when it seems like you are unprepared. You Interact to reload your hand crossbow or gauntlet bow and attempt a ranged Strike with it.

**Special** If you have the Repeating Hand Crossbow Training feat, you can use this feat with a repeating hand crossbow to load an entire magazine, but the speed means you can fire only one bolt before the magazine jams and becomes useless. You must fully replace a magazine as normal before firing with a repeating hand crossbow after using this ability.

**Source:** `= this.source` (`= this.source-type`)
