---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sniping Duo|Sniping Duo]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Sniping Duo Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You or your spotter misses with a Strike against a creature, and the creature is within the other's melee reach or first range increment.

Your skilled teamwork with your spotter enables you both to assist one another when you falter, using either other's failures as opportunities to strike. If you used Tag Team after your spotter missed the triggering Strike, make a ranged Strike against the same target with a -2 penalty. If you used this reaction after you missed the triggering Strike, your spotter can use their reaction to make a melee or ranged Strike against the same target. Strikes granted by this feat don't count toward your or your spotter's multiple attack penalty and your or your spotter's multiple attack penalty doesn't apply to the granted Strike.

**Source:** `= this.source` (`= this.source-type`)
