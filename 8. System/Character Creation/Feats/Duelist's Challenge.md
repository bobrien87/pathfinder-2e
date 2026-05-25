---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Duelist|Duelist]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Duelist Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Select one enemy you can see and proclaim a challenge against it. That enemy is your dueling opponent until it's defeated, it flees from the encounter, or the encounter ends. Any time you hit that enemy using a single one-handed melee weapon while your other hand or hands are free, you gain a circumstance bonus to the Strike's damage equal to the number of damage dice your weapon deals.

If you attack a creature other than your dueling opponent, you take a circumstance penalty to damage equal to the number of damage dice your weapon deals.

**Source:** `= this.source` (`= this.source-type`)
