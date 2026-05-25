---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Guerrilla|Guerrilla]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Guerrilla Dedication, expert in Stealth"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are unnoticed or undetected by your target.

Leaping from a hiding place, you quickly attack your foe before retreating. You Stride or Step, then attempt a melee or ranged Strike against a creature. After your Strike, you [[Sneak]] away. None of the movement taken as part of this activity triggers reactions.

**Source:** `= this.source` (`= this.source-type`)
