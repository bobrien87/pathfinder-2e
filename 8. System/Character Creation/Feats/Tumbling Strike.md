---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Acrobat|Acrobat]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Flourish]]", "[[Move]]"]
prerequisites: "Acrobat Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are adjacent to an enemy.

You deftly dive through a gap left by a foe to deliver an advantageous blow. Attempt an Acrobatics check against the Reflex DC of an enemy adjacent to you.
- **Critical Success** You move through the enemy's space to an unoccupied space on the other side of the enemy from your starting position. This movement doesn't trigger reactions. You can't move farther than your Speed, and you must end your movement adjacent to the enemy whose space you moved through. After moving, you make a melee Strike against the enemy whose space you moved through, and the enemy is [[Off Guard]] against that Strike.
- **Success** As critical success, but the enemy isn't off-guard against the Strike.
- **Failure** You remain in your original space but can still Strike.
- **Critical Failure** You neither move nor Strike.

**Source:** `= this.source` (`= this.source-type`)
