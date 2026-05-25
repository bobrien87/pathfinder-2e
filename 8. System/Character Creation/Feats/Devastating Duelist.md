---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Aldori Duelist|Aldori Duelist]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Aldori Duelist Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You pointedly note your enemy's deficiencies, filling them with fear and dismay. Strike an opponent with your [[Aldori Dueling Sword]].

If the Strike is successful, attempt a Dueling lore check{Dueling Lore} check against the target's Will DC. On a success, the target becomes [[Frightened]] 2. This is an emotion, fear, and mental effect.

**Source:** `= this.source` (`= this.source-type`)
