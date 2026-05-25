---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wild Mimic|Wild Mimic]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Wild Mimic Dedication, you have seen a creature use Rend or have identified a creature that has Rend in combat"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have hit the same enemy with two consecutive melee Strikes that each dealt slashing damage.

Taking advantage of the brutal efficiency of hacking away at a target with two slashing attacks, you've mastered the art of punishing a foe caught between your slices. You deal @Damage[(ternary(gte(@actor.level,16),3,ternary(gte(@actor.level,10),2,1)))d6[slashing]] damage to the target. This damage increases to 2d6 at 10th level and to 3d6 at 16th level.

**Source:** `= this.source` (`= this.source-type`)
