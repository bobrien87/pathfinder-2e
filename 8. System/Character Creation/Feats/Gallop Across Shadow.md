---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Nidalese Horselord|Nidalese Horselord]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Occult]]"]
prerequisites: "Nidalese Horselord Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Though your enemy wields shadow and darkness as weapons, they are no impediment to you when you ride your trusted horse. To that end, your mount can step onto patches of darkness as if they were solid. When your horse moves through an area of darkness, it can treat empty spaces as solid ground. This allows your horse to move across gaps bridged by darkness or even into the air, ascending or descending at a maximum of a 45-degree angle. If your horse isn't on actual solid ground and the area your horse is in becomes dim light or brighter, your horse falls.

**Source:** `= this.source` (`= this.source-type`)
