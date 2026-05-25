---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Winged Warrior|Winged Warrior]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Winged Warrior Dedication"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** tengu, strix, or awakened animal (flying animal) ancestry

The skies are your rightful place, and you will not suffer another to occupy them. Make a Strike against a flying creature. If the attack deals damage, the target must attempt a [[Reflex]] save against your class DC.
- **Critical Success** No effect.
- **Success** The target falls 15 feet but doesn't take damage if it reaches the ground.
- **Failure** The target falls 30 feet but doesn't take damage if it reaches the ground.
- **Critical Failure** As failure, but the target takes falling damage.

**Source:** `= this.source` (`= this.source-type`)
