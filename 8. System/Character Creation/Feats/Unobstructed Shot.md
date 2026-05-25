---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Archer|Archer]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Archer Dedication, expert in Athletics"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a quick use of brute force, you remove an obstacle and take a calculated shot as part of the same motion. Attempt to [[Shove]] or [[Trip]] one adjacent creature, then make a ranged Strike with a bow or crossbow you're wielding. The Strike is made at the same multiple attack penalty as the Shove or Trip attempt, and this activity counts as one attack when calculating your multiple attack penalty.

**Source:** `= this.source` (`= this.source-type`)
