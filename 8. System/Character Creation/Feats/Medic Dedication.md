---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Medic|Medic]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Medicine, Battle Medicine"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You become an expert in Medicine. When you succeed with [[Battle Medicine]] or [[Treat Wounds]], the target gains a circumstance bonus to the number of Hit Points they regain equal to 5 HP at DC 20, 10 HP at DC 30, or 15 HP at DC 40.

Once per day, you can use Battle Medicine on a creature that's temporarily immune due to having already been treated with Battle Medicine. If you're a master in Medicine, you can do so once per hour.

Medic

**Source:** `= this.source` (`= this.source-type`)
