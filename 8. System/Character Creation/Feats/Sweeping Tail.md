---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beastmaster|Beastmaster]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Beastmaster Dedication, animal companion with a tail unarmed attack"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your companion swings its tail powerfully. Your companions with a qualifying unarmed attack learn the Sweeping Tail activity.

**Sweeping Tail** `pf2:2` This companion makes two tail Strikes against different creatures within its reach, increasing its multiple attack penalty as normal. On a hit, it pushes a target back 5 feet or 10 feet on a critical hit. This is forced movement.

**Source:** `= this.source` (`= this.source-type`)
