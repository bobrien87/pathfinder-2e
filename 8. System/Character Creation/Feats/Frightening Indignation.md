---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Steel Falcon|Steel Falcon]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Aura]]", "[[Divine]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]"]
prerequisites: "Steel Falcon Dedication"
frequency: "once per day"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Your anger at the world's many injustices boil out from you in a wave of palpable energy. An enemy that ends its turn within a @Template[type:emanation|distance:15] around you must attempt a [[Will]] save against your class DC or spell DC, whichever is higher. This aura lasts for 1 minute.
- **Critical Success** The creature is unaffected and becomes temporarily immune to your Frightening Indignation for 1 minute.
- **Success** The creature is [[Frightened]] 1.
- **Failure** The creature is [[Frightened]] 2 and can't reduce its frightened condition below 1 while it's in your aura.
- **Critical Failure** As failure, but [[Frightened]] 3.

**Source:** `= this.source` (`= this.source-type`)
