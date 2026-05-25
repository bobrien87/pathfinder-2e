---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Cultivator|Cultivator]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Occult]]"]
prerequisites: "Cultivator Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Attuned to all arrangements of qi, you gain lifesense as an imprecise sense with a range of 30 feet. You can also sense the presence of precious materials in the same range, which cultivators refer to as "cultivation materials."

When you participate in rituals, you can substitute all or part of the ritual's cost with an equivalent value of precious materials. This applies only to costs in valuable substances like diamonds, not to rituals that require specific items to function; the GM makes the call if it's unclear.

**Source:** `= this.source` (`= this.source-type`)
