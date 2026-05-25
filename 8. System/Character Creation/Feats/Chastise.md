---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mortal Herald|Mortal Herald]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Sanctified]]"]
prerequisites: "Fear of God"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With but a mere word from your deity, you exploit a foe's fear to see their inner being brought low. You chastise the spirit of a foe within 30 feet that has the frightened condition. The target must attempt a [[Will]] save saving throw against the higher of your class DC or spell DC. The target is then temporarily immune for 1 hour.
- **Critical Success** The target is unaffected.
- **Success** The target takes 2 persistent,spirit damage. The first time the creature fails their flat check to recover from this, the persistent spirit damage doubles.
- **Failure** The target takes 4 persistent,spirit damage. The first time the creature fails their flat check to recover from this, the persistent spirit damage doubles.
- **Critical Failure** The target takes 6 persistent,spirit damage. The first time the creature fails their flat check to recover from this, the persistent spirit damage doubles.

**Source:** `= this.source` (`= this.source-type`)
