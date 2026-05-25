---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Archfiend|Archfiend]]"
source-type: "Remaster"
level: "18"
traits: ["[[Mythic]]", "[[Teleportation]]"]
prerequisites: "Archfiend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your last action dealt damage to a creature.

Rather than grant your foes the mercy of a swift death, you can consign them to suffer in an extradimensional prison with an appearance of your choosing. Spend 1 Mythic Point to force a creature that you dealt damage to with your last action to attempt a [[Will]] save saving throw against your class DC or spell DC, whichever is higher. Regardless of the result, the target is temporarily immune to your Imprison Foe for 24 hours.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Stunned]] 2.
- **Failure** The target is transported into a cell within your extradimensional dungeon for 1 minute. It is unable to leave or damage the cell in any way. Teleportation effects can't carry the target outside the cell unless they can also traverse the planes, such as interplanar teleport. At the end of each of its turns, it can attempt a new Will save to reduce the remaining duration it is imprisoned by 1 round or end it entirely on a critical success. When the duration ends, the target returns to the space it occupied when it was imprisoned, or to the nearest space if the original is now filled.
- **Critical Failure** As failure, but the target is stunned for the first round it is imprisoned.

**Source:** `= this.source` (`= this.source-type`)
