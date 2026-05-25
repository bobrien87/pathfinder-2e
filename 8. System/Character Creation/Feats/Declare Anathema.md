---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mortal Herald|Mortal Herald]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Curse]]", "[[Divine]]"]
prerequisites: "Mortal Herald Dedication"
frequency: "once per PT10M"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

You declare a creature you are aware of within 30 feet anathema, causing their friends and strangers to shy away from them. Attempt a [[Religion]] check against the target's Will DC.
- **Critical Success** Any creature that attempts to target the anathema creature with a beneficial effect must succeed at a DC 5 flat check or the action is disrupted. This curse remains until removed by [[Cleanse Affliction]] or a similar effect, or an atone ritual. In addition, the creature gains weakness 10 to spirit damage for 1 minute.

> [!danger] Effect: Declare Anathema
- **Success** As critical success, but the curse lasts for 1 minute.
- **Failure** As critical success, but the curse lasts for 1 round and the target doesn't gain weakness to spirit damage.
- **Critical Failure** The target is unaffected.

**Source:** `= this.source` (`= this.source-type`)
