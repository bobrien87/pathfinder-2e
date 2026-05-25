---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sister Of The Golden Erinys|Sister Of The Golden Erinys]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Concentrate]]", "[[Divine]]", "[[Linguistic]]", "[[Mental]]", "[[Nonlethal]]"]
prerequisites: "Sister of the Golden Erinys Dedication"
frequency: "once per PT1M"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per minute

You call out to an enemy in distress, promising them a future of unending pain. Choose an enemy with the sickened condition that you can see within 120 feet. That creature takes @Damage[max(10,(floor(@actor.level/2)*2))d4[mental]] damage with a [[Will]] save against your class DC or spell DC, whichever is higher. At 12th level and every 2 levels thereafter, the damage increases by 2d4.

**Source:** `= this.source` (`= this.source-type`)
