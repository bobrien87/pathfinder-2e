---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Animist]]", "[[Apparition]]", "[[Divine]]", "[[Fire]]", "[[Wandering]]"]
frequency: "once per PT10M"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

**Trigger** A creature damages you with a melee attack.

**Requirements** Your attuned apparition grants Battlegrounds Lore or Volcano Lore as an apparition skill.

Your apparition grants fiery defenses. You gain resistance equal to your level against the triggering damage, and the triggering creature takes @Damage[(ternary(gte(@actor.level,18),3,ternary(gte(@actor.level,12),2,1)))d6[fire],(ternary(gte(@actor.level,18),3,ternary(gte(@actor.level,12),2,1)))[persistent,fire]] damage. This damage increases to 2d6 fire damage and 2 persistent fire damage at 12th level, and 3d6 fire damage and 3 persistent fire damage at 18th level.

**Source:** `= this.source` (`= this.source-type`)
