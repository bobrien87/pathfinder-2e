---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ostilli Host|Ostilli Host]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Ostilli Host Dedication"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your ostilli's darts can deal different types of damage. When you Spit Ambient Magic, you can choose to have the ostilli deal bludgeoning or slashing damage instead of piercing damage. At 8th level, choose one of the following: acid, cold, electricity, fire, or sonic damage; when your ostilli Spits Ambient Magic, it can deal that damage type instead and adds that trait to the action.

**Special** You can take this feat a second time at 16th level. When you do, choose two additional energy types from those available through this feat at 8th level; you can choose to have your ostilli deal that damage type when it Spits Ambient Magic.

**Source:** `= this.source` (`= this.source-type`)
